from rest_framework import serializers


class UserActivitySerializer(serializers.Serializer):
    """
    Yes, this is not a `ModelSerializer`.
    """
    last_login = serializers.SerializerMethodField()
    last_request = serializers.SerializerMethodField()

    def get_last_login(self, obj):
        return obj.last_login

    def get_last_request(self, obj):
        return obj.last_request
