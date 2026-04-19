from django.db import models

# Create your models here.
class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        