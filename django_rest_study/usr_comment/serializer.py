# coding: utf-8

from rest_framework import serializers

from .models import Comment,Comment_Score


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment_id','usr_id','comment')


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment_Score
        fields = ('comment_id','score_type','score')