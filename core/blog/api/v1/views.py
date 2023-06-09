from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly #, IsAdminUser=is staff
from rest_framework.response import Response
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from rest_framework import status, mixins, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination
#Example for ViewSet in CBV
class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class=PostSerializer     
    queryset=Post.objects.filter(status=True)   
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = { "category": ["exact","in"],"author": ["exact"],"status": ["exact"]  }
    search_fields = ['=title', 'content']  # = means exact match
    ordering_fields = ['published_date']
    pagination_class = DefaultPagination




class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class=CategorySerializer     
    queryset=Post.objects.all()

























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
'''
@api_view(['GET','PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])  
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
        return Response({'detail':'item remove successfully'},status=status.HTTP_204_NO_CONTENT )    '''
'''
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])               #must be after api_view decorator
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
        return Response(serializer.data)'''




"""class PostDetail(APIView):
    '''getting detail of the post and edit plus removing it '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class=PostSerializer     

    def get(self, request, id):
        '''retrieving the post data'''
        post=get_object_or_404(Post, pk=id)
        serializer=self.serializer_class(post)          #self.serializer_class==PostSerializer
        return Response(serializer.data)
    def put(self, request, id):
        '''editing the post data'''
        post=get_object_or_404(Post, pk=id)
        serializer=PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True) 
        serializer.save()
        return Response(serializer.data)         
        '''deleting the post data'''
    def delete(self, request, id):
        post=get_object_or_404(Post, pk=id)
        post.delete()   
        return Response({'detail':'item remove successfully'},status=status.HTTP_204_NO_CONTENT )"""

class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class=PostSerializer     
    queryset=Post.objects.filter(status=True)   
    #lookup_field='id'            #or change id to pk in the url


"""class PostList(APIView):
    '''getting a list of posts and creating a new posts '''

    permission_classes = [IsAuthenticated]
    serializer_class=PostSerializer              #create a form for post
    def get(self, request):
        '''retrieving a list of posts  '''
        post=Post.objects.filter(status=True)
        serializer=PostSerializer(post, many=True)
        return Response(serializer.data)        

    def post(self, request):
        '''creating a post with a provided data '''
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)"""

# class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin ):
#     permission_classes = [IsAuthenticated]
#     serializer_class=PostSerializer     
#     queryset=Post.objects.filter(status=True)        
#     def get(self, request, *args, **kwargs):
#         queryset=self.get_queryset()
#         return self.list(request, *args, **kwargs)        
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)  
"""class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class=PostSerializer     
    queryset=Post.objects.filter(status=True)   """

