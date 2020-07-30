from django.db import models

# Create your models here.
class product(models.Model):
    title       = models.CharField(max_length =119)
    description = models.TextField(blank=True,null=True)
    price       = models.DecimalField(max_digits=9999,decimal_places=2)
    summary     = models.TextField()

