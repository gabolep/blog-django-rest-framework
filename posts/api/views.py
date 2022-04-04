from cgitb import lookup
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Post
from posts.api.serializers import PostSerializer
from blog.utils.permissions import IsAdminOrReadOnly

class PostApiViewsSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published = True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category','category__slug']
    