from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.fields.TextField(max_length=200)
    def __str__(self):
        return self.text[:50]
