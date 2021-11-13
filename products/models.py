from django.db import models
from django.shortcuts import reverse


class Product(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    price = models.PositiveIntegerField()
    prod_location = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    description = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to=None)

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('date_pub',)


class Categories(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)


class Comment(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', null=True)
    comment_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
