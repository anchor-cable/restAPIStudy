# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from .models import Comment,Comment_Score
from .serializer import UserSerializer, EntrySerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = UserSerializer


class Comment_ScoreViewSet(viewsets.ModelViewSet):
    queryset = Comment_Score.objects.all()
    serializer_class = EntrySerializer