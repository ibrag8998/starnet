from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser

from users.serializers import UserActivitySerializer


class UserViewSet(DjoserUserViewSet):
    @action(['get'], detail=True, permission_classes=[IsAdminUser], serializer_class=UserActivitySerializer)
    def activity(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
