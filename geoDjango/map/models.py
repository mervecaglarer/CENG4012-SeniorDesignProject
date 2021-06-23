from django.db import models

# Create your models here.
class Doc(models.Model):
    ip = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    date = models.DateField()

    def __str__(self):
        return self.country