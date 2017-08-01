from django.contrib.auth.models import User
from django.db import models


SHORT_TEXT = 1000

class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User)


    @property
    def __str__(self):
        return self.title

    def short_text(self):
        if len(self.text) > SHORT_TEXT:
            return self.text[:SHORT_TEXT]
        else:
            return self.text

