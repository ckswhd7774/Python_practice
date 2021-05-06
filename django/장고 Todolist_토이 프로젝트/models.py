from django.db import models

# Create your models here.

class TodoList(models.Model) : 
    todo = models.CharField(max_length=30)
    
    def __str__(self) :
        return self.todo