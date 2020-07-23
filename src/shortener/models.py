from django.db import models

# Create your models here.
class KirrURL(models.Model):
    url = models.CharField(max_length=220, )
    shortened = models.CharField(max_length=15, unique=True)
    last_updated = models.DateTimeField(auto_now=True) #everytime model is saved
    timestamp = models.DateTimeField(auto_now_add=True) #when model was created

    def __str__(self):
        return str(self.url)
