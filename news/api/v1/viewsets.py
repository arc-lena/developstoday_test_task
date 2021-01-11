from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated


from news.models import Post, Comment
from news.api.v1.serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("author_name")
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]
    serializer = PostSerializer(queryset)

    def perform_create(self, serializer):
        serializer.save(author_name=self.request.user)

    @action(detail=True, methods=["post"])
    def upvote(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        post.amount_of_upvotes += 1
        post.save()
        return Response({"message": "amount changed"})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("author_name")
    serializer_class = CommentSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]
    serializer = CommentSerializer(queryset)

    def perform_create(self, serializer):
        serializer.save(author_name=self.request.user)
