from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from posts.filtersets import LikeFilterSet
from posts.models import Post, Like
from posts.serializers import PostSerializer, LikeSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(['post'], detail=True, serializer_class=None)
    def like(self, request, *args, **kwargs):
        data = {'user': self.request.user.id, 'post': self.get_object().id}
        serializer = LikeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(['post'], detail=True, serializer_class=None)
    def unlike(self, request, *args, **kwargs):
        try:
            Like.objects.get(user=self.request.user.id, post=self.get_object().id).delete()
        except Like.DoesNotExist:
            return Response({"non_field_error": "You haven't liked this post, so you cannot unlike"},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


class LikeViewSet(ReadOnlyModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = LikeFilterSet
