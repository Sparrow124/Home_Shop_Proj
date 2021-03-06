# Generated by Django 3.2.9 on 2021-11-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='products', to='products.Categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='images'),
        ),
    ]
