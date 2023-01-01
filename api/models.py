from django.db import models

# Create your models here.
class Location(models.Model):
    locationName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.locationName

class Item(models.Model):
    ItemName = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)
    itemLocatrion = models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return self.ItemName