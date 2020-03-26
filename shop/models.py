from django.db import models

class Category(models.Model):
    slug = models.SlugField(default='')
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children',on_delete=models.CASCADE)
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title