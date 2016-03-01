from django.db import models

# Create your models here.

class Login(models.Model):

    text = models.TextField()
    password = models.TextField()
    
    def validatelogin(self):
        
            return True
    
