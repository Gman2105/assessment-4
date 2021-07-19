from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return f"{self.name}"
        
class Post(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 50)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'posts')
    
    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}"
