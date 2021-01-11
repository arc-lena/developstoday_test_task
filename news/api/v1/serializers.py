from rest_framework import serializers
from news.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "link",
            "creation_date",
            "author_name",
            "amount_of_upvotes",
        )
        read_only_fields = ("author_name",)

    @staticmethod
    def get_author_name(obj):
        return obj.author_name.username


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "content", "post", "creation_date", "author_name")
        read_only_fields = ("author_name",)

    @staticmethod
    def get_author_name(obj):
        return obj.author_name.username
