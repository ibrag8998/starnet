import warnings

from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Post, Like

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    users_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author']

    def get_users_liked(self, obj):
        return User.objects.filter(likes__post=obj).values_list('id', flat=True)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

    def update(self, instance, validated_data):
        warnings.warn("`Like` instance cannot be updated manually")
        return instance
