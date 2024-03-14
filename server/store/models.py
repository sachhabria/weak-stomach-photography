from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='prints/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title

class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    length = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.product.title}, {self.length}\"x{self.width}\""
