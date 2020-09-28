from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()


class ShoeType(models.Model):
    style = models.CharField(max_length=20)


class ShoeColor(models.Model):
    color_name = models.CharField(max_length=10, choices=[('RED', 'red'), ('ORANGE', 'Orange'), ('YELLO', 'Yello'), ('GREEN', 'Green'), (
        'BLUE', 'Blue'), ('INDIGO', 'Indigo'), ('VIOLET', 'Violet'), ('WHITE', 'White'), ('BLACK', 'Black')])


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=50)
