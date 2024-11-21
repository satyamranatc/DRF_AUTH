from django.db import models

# Create your models here.
class ProgrmmingCard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
