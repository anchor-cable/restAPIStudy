# coding: utf-8

from rest_framework import routers
from .views import CommentViewSet, Comment_ScoreViewSet

app_name = 'usr_comment'
router = routers.DefaultRouter()
router.register(r'comment', CommentViewSet)
router.register(r'comment_score', Comment_ScoreViewSet)