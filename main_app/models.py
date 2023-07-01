from django.db import models

class Author(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=20000)
    bio = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']