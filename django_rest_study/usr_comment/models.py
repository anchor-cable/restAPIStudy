from django.db import models

class Comment(models.Model):
    comment_id = models.IntegerField(null=True)
    usr_id = models.IntegerField(null=True)
    comment_date = models.DateField(null=True)
    comment = models.TextField(max_length=2000) # ToDo UTF-8の指定入れる

class Comment_Score(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    score_type = models.IntegerField(null=True)
    score = models.FloatField(null=True)




# Create your models here.
