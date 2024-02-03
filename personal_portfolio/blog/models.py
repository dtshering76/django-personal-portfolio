from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_posted = models.DateField()
    content = models.TextField()
    
    def __str__(self):
        return self.title
    