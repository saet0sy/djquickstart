from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.title

class Meta:
    verbose_name_plural = "Products"