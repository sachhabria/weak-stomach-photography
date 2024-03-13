from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=200)
    img_url = models.CharField("image url", max_length=100)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title

class Size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    length = models.PositiveIntegerField(default=0)
    width = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.product.title} in size {self.length}\"x{self.width}\""
    