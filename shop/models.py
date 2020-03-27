from django.db import models


class Category(models.Model):
    slug = models.SlugField(default='')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='static/images', null=True, blank=True)
    description = models.TextField( default=" ")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.title


