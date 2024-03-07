from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    year = models.IntegerField(null=True) #1956

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField() #1890
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def clean(self):
        if self.year < 0:
            raise ValidationError("rok poniżej zera")
