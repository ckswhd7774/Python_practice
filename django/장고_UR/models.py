from django.db import models

# Create your models here.

class Home(models.Model) :
    category_name = models.CharField(max_length=30)

    def __str__(self) :
        return self.category_name

class Category(models.Model) :
    article = models.ForeignKey('Home', on_delete=models.CASCADE,related_name='article')
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=30)

    def __str__(self) :
        return self.title