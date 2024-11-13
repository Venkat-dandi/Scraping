from django.db import models

class NewsItem(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
