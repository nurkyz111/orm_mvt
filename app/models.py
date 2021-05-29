from django.db import models
from PIL import Image
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Category')
    slug = models.SlugField(max_length=50, verbose_name='Slug', unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='product')
    name = models.CharField(max_length=25, verbose_name='Name')
    description = models.TextField(verbose_name='description')
    image = models.ImageField(upload_to='products/', verbose_name='Image', default='default.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])
