from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404


# @api_view()
# def postList(request):
#     return Response('OK GUY!')


# @api_view()
# def postDetail(request, id):
#     post=Post.objects.get(pk=id)
#     print(post.__dict__)             #__dict__ showes all itemes in  the object
#     serializer=PostSerializer(post)
#     print(serializer.__dict__)
#     print(serializer.data)
#     return Response(serializer.data)

# @api_view()
# def postDetail(request, id):
#     try:
#         post=Post.objects.get(pk=id)
#         serializer=PostSerializer(post)       
#         return Response(serializer.data)
#     except Post.DoesNotExist:
#         return Response({'detail':'post does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','PUT', 'DELETE'])
def postDetail(request, id):
    post=get_object_or_404(Post, pk=id)
    if request.method=="GET":
        serializer=PostSerializer(post)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer=PostSerializer(post, data=request.data)  #if you do not use post, it be created rather than updating
        serializer.is_valid(raise_exception=True) 
        serializer.save()
        return Response(serializer.data) 
    elif request.method=="DELETE":
        post.delete()   
        return Response({'detail':'item remove successfully'},status=status.HTTP_204_NO_CONTENT )    


@api_view(['GET', 'POST'])
def postList(request):
    if request.method=="GET":
        post=Post.objects.filter(status=True)
        serializer=PostSerializer(post, many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=PostSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors)
        serializer.is_valid(raise_exception=True)   #paranthesis means if it is ok go on, else show errors
        serializer.save()
        return Response(serializer.data)
