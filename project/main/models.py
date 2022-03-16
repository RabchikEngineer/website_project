from django.db import models

# Create your models here.

# class StandartProduct(models.Model):
#     price=models.DecimalField(max_digits=10,decimal_places=2,db_index=True)
#     weight=models.DecimalField(max_digits=10,decimal_places=2,db_index= True)


class Tractor(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    power=models.IntegerField(db_index=True)
    units_of_power=models.CharField(max_length=7)
    engine_cycle=models.IntegerField()
    number_of_front_gears=models.IntegerField()
    number_of_rear_gears=models.IntegerField()
    downshift=models.BooleanField()
    PTO=models.BooleanField()  #вал отбора мощности