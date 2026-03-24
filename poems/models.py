from django.db import models

# Create your models here.
class Poet(models.Model):
    name_en = models.CharField(max_length=100)
    name_mm = models.CharField(max_length=100)    # Myanmar name
    about = models.TextField(blank=True)          # About the poet
    
    def __str__(self):
        return self.name_en

class Poem(models.Model):
    title_en = models.CharField(max_length=200)
    title_mm = models.CharField(max_length=200)  # Myanmar title
    poem_mm = models.TextField()                  # Myanmar poem content
    poem_en = models.TextField()                  # English poem content
    about = models.TextField(blank=True)          # About the poem
    source = models.CharField(max_length=200, blank=True)
    featured = models.BooleanField(default=False)  # True/False column
    # FIXED: Changed from 'poets.Poet' to 'Poet'
    poet = models.ForeignKey('Poet', on_delete=models.CASCADE, related_name='poems')
    date_added = models.DateTimeField("date added")
    
    def __str__(self):
        return self.title_en