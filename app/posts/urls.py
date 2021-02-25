from rest_framework.routers import SimpleRouter

from posts.views import PostViewSet, LikeViewSet

r = SimpleRouter()
r.register('posts', PostViewSet)
r.register('likes', LikeViewSet)

app_name = 'posts'

urlpatterns = [
    *r.urls,
]
