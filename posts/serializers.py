from rest_framework import serializers
from .models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    postedBy = serializers.ReadOnlyField(source='postedBy.username')
    postedBy_id = serializers.ReadOnlyField(source='postedBy.id')
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'postedBy', 'postedBy_id', 'created','votes']

    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']
