from django.contrib import admin
from .models import Comment,Comment_Score

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment_Score)
class Comment_ScoreAdmin(admin.ModelAdmin):
    pass