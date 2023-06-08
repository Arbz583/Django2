from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile

# class PostSerializer(serializers.Serializer):
#     id=serializers.IntegerField()
#     title = serializers.CharField(max_length=255)



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields = ('id',)
       # read_only_fields=['name']


class PostSerializer(serializers.ModelSerializer):
    snippet=serializers.ReadOnlyField(source='get_snippet')
    relative_url=serializers.URLField(source='get_absolute_api_url', read_only=True)
    absolute_url=serializers.SerializerMethodField(method_name='getabs_url') #if you do not use method_name you should use get_ to define relative function
    category=serializers.SlugRelatedField(many=False,slug_field='name',queryset=Category.objects.all())  #CategorySerializer()
    class Meta:
        model=Post
        fields=['id', 'author','title','content','snippet','category', 'status','relative_url','absolute_url', 'published_date' ]
        read_only_fields=['author']

    def getabs_url(self, obj):
        request=self.context.get('request')
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        rep=super().to_representation(instance)
        request=self.context.get('request')
        if request.parser_context.get('kwargs').get('pk'):       #if pk be sended in the url.
            rep.pop('snippet',None)
            rep.pop('relative_url',None)
            rep.pop('absolute_url',None)
        else:
            rep.pop('content',None)
        rep['category']=CategorySerializer(instance.category, context={'request':request}).data         
        return rep
    
    def create(self, validated_data):
        print(self.context.get('request').user.id)
        validated_data['author']=Profile.objects.get(user__id=self.context.get('request').user.id)
        return super().create(validated_data)

