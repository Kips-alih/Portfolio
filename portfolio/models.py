from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    screenshot=CloudinaryField('image',default='Image')
    topics=models.CharField(max_length=200,null=True)
    description = models.TextField(max_length=300,null=True)
    live_link = models.CharField(max_length=50,null=True)

      
    def __str__(self):
        return self.name
    
    def save_project(self):
        self.save()
