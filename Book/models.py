from django.db import models
# Create your models here.

class Booksmodel(models.Model):
    name = models.CharField(max_length=11)
    author = models.CharField(max_length=10)
    copies = models.IntegerField()


    

