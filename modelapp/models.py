from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField('date')

    # admin 글 제목 표시
    def __str__(self):
        return self.title