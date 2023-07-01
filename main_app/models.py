from django.db import models

class Author(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=20000)
    bio = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Book(models.Model):

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=20000, default='default_image.html')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title
    

class Readinglist(models.Model):

    title = models.CharField(max_length=150)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.title  