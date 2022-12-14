from django.db import models

class product(models.Model):
    name = models.CharField(max_length=150)
    count = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=4)

    class Meta:
        verbose_name ='Kategorii'
        verbose_name_plural = 'kategoriya'

    def __str__(self):
        return f'{self.id} - {self.name}'
# Create your models here.
