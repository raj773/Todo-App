from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TODO(models.Model):
    status_choices = [
    ('C','Completed'),
    ('P','Pending'),
    ]
    
    title = models.CharField(max_length=50)
    status = models.CharField(choices=status_choices, default="P", max_length=2)
    user  = models.ForeignKey(User  , on_delete= models.CASCADE)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
    Deadline = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))


    class Meta:
        verbose_name  = "user"
        verbose_name_plural = "users"
        
    def __str__(self):
        return self.title

    
