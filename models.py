from django.db import models

# Create your models here.
class Proddesc(models.Model):
  productId = models.IntegerField()
  category = models.CharField(max_length=20)
  shippingPrice = models.IntegerField()
  deliveryTime = models.IntegerField()
  price=models.IntegerField()
  tax=models.IntegerField()
  site1=models.IntegerField(default=2000)
  site2=models.IntegerField(default=2300)
  site3=models.IntegerField(default=2200)

  def __str__(self):
  	string=str(self.productId)
  	return string


