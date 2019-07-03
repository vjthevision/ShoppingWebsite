from django.db import models
from django.urls import reverse

# Create your models here.
class Laptop(models.Model):
    title = models.CharField(max_length=120)
    desc = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to='pics')
    featured = models.BooleanField(default=False)
    category_name = models.CharField(max_length=120,default='Laptop')
    def get_absolute_url(self):
        return reverse("laptops:product-detail", kwargs={"id": self.id})

class Category(models.Model):

    name = models.ForeignKey(Laptop,on_delete=models.CASCADE)

    def get_absolute_url1(self):
        return reverse("laptops:category-detail",kwargs={"id": self.id})