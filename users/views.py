from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

from .models import Post
from .serializers import PostSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return super().get_permissions()


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def _check_authorization(self):
        post = self.get_object()
        if post.author != self.request.user:
            raise PermissionDenied(
                "Вы не можете редактировать или удалить этот пост."
            )

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()

    def perform_update(self, serializer):
        self._check_authorization()
        serializer.save()

    def perform_destroy(self, instance):
        self._check_authorization()
        instance.delete()
