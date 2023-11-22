from django.db import models
from django.utils.text import slugify

# Create your models here
class Meals(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    available = models.CharField(max_length=10)
    image = models.ImageField(upload_to='media/meals')
    slug = models.SlugField(blank=True,null=True)

    def save(self, *args, **kw):
        if not self.slug and self.name:
            self.name = slugify(self.name)
        super (Meals, self).save(*args, **kw)

    class Meta:
        verbose_name = 'meal'
        verbose_name_plural = 'meals'



    def __str__(self):
       return self.name



