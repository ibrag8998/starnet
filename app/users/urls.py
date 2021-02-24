from rest_framework.routers import SimpleRouter

from users.views import UserViewSet

r = SimpleRouter()

r.register('users', UserViewSet)

app_name = 'users'

urlpatterns = [
    *r.urls
]
