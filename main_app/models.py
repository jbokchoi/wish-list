from django.db import models
from django.urls import reverse

# Create your models here.
class Wish(models.Model):
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.wish
    
    def get_absolute_url(self):
        return reverse('/', kwargs={'wish_id': self.id})