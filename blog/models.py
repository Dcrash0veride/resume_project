from django.db import models
import datetime

class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_author = models.CharField(max_length=20)
    blog_date = models.DateField("Date", default=datetime.date.today)
    blog_post = models.TextField(max_length=10000)

    def __str__(self):
        return self.blog_title