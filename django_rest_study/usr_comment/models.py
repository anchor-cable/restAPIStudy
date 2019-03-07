from django.db import models

class Entry(models.Model):
    comment_id = models.IntegerField
    usr_id = models.IntegerField
    comment_date = models.DateTimeField
    comment = models.TextField(max_length=2000) # ToDo UTF-8の指定入れる



# Create your models here.
