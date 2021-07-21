from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=250)
    isbn_number = models.CharField(max_length=13)


    def __str__(self):
        return self.name
