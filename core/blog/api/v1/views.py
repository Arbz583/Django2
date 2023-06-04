from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post


@api_view()
def postList(request):
    return Response('OK GUY!')

@api_view()
def postDetail(request, id):
    post=Post.objects.get(pk=id)
    print(post.__dict__)             #__dict__ showes all itemes in  the object
    serializer=PostSerializer(post)
    print(serializer.__dict__)
    print(serializer.data)
    return Response(serializer.data)