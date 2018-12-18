from django.db import models


class Author(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='saugat.jpg', blank= True)

    def __str__(self):
        return self.title

