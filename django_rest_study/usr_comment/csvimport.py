import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproj.settings")

import csv
from usr_comment.models import Comment

reader = csv.reader(open("user_comment.csv"))

for r in reader:
    print
    r
    c = Comment()
    c.comment_id = r[0].decode('cp932').encode('utf-8')
    c.usr_id= r[1]
    c.comment_date = r[2]
    c.comment = r[3]
    c.save()
