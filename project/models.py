from django.db import models
# project/models.py
# Create your models here.
class Project(models.Model):
    medium_url = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.medium_url
