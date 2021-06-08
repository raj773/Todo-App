from django.db import models
from django.utils import timezone
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)    
    deadline = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    created_at = models.DateTimeField(auto_now=True)