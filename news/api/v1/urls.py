from news.api.v1 import viewsets
from django.urls import path, include
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register("post", viewsets.PostViewSet, basename="post")
router.register("comment", viewsets.CommentViewSet, basename="comment")

urlpatterns = [
    path("", include(router.urls)),
]
