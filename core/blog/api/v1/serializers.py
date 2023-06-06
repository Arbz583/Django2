from rest_framework import serializers
from ...models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']
        read_only_fields=['name']
# class PostSerializer(serializers.Serializer):
#     id=serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class PostSerializer(serializers.ModelSerializer):
    snippet=serializers.ReadOnlyField(source='get_snippet')
    relative_url=serializers.URLField(source='get_absolute_api_url', read_only=True)
    absolute_url=serializers.SerializerMethodField(method_name='getabs_url') #if you do not use method_name you should use get_ to define relative function
    category=CategorySerializer()     #serializers.SlugRelatedField(many=False,slug_field='name',queryset=Category.objects.all())
    class Meta:
        model=Post
        fields=['id', 'author','title','content','snippet','category', 'status','relative_url','absolute_url', 'published_date' ]


    def getabs_url(self, obj):
        request=self.context.get('request')
        return request.build_absolute_uri(obj.pk)

