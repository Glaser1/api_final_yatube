from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, GroupViewSet, FollowViewSet, CommentViewSet


v1_router = DefaultRouter()

v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)
v1_router.register('follow', FollowViewSet, basename='subscriptions')
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename='comments'
                   )


urlpatterns = [
    path('', include(v1_router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
