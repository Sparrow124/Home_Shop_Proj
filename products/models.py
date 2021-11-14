from django.db import models
from django.shortcuts import reverse


class Product(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    price = models.PositiveIntegerField()
    prod_location = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='images')
    categories = models.ManyToManyField('Categories', blank=True, related_name='products')

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('date_pub',)


class Categories(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', null=True)
    comment_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
