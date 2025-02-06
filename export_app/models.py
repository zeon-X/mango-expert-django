from django.db import models

class MangoExport(models.Model):
    variety = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.variety
