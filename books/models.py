from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length = 150)
    subtitle = models.CharField(max_length = 150)
    author = models.CharField(max_length = 150)
    isbn = models.CharField(max_length = 40)

# Allows title of the book to display in admin.
    def __str__(self):
        return self.title
