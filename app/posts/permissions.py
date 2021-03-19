from rest_framework.permissions import IsAuthenticated

from posts.models import Post, Like


class IsPostAuthor(IsAuthenticated):
    def has_object_permission(self, request, view, obj: Post):
        return obj.author == request.user


class IsLikeAuthor(IsAuthenticated):
    def has_object_permission(self, request, view, obj: Like):
        return obj.user == request.user
