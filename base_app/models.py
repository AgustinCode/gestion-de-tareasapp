from django.db import models

class task(models.Model):
    name=models.CharField(max_length=200)
    creation_date=models.DateField()
    

# Create your models here.
