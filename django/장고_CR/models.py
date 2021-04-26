from django.db import models

# Create your models here.
class HomePage(models.Model) :
    category_num = models.IntegerField()
    category_name = models.CharField(max_length=30)

    def __str__(self) :
        return self.category_name

class Category(models.Model) :
    article = models.ForeignKey('Homepage', on_delete=models.CASCADE, related_name='article')
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=20)

    def __str__(self) :
        return self.title