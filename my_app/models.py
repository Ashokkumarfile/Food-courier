from itertools import product
from django.db import models
from django.contrib.auth.models import User
import datetime
import os
 

def getFileName(requset,filename):
  now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
  new_filename="%s%s"%(now_time,filename)
  return os.path.join('uploads/',new_filename)

class Catagory(models.Model):
  name=models.CharField(max_length=150,null=False,blank=False)
  image=models.ImageField(upload_to=getFileName,null=True,blank=True)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  created_at=models.DateTimeField(auto_now_add=True)
  
  def __str__(self) :
    return self.name
 
class Product(models.Model):
  category=models.ForeignKey(Catagory,on_delete=models.CASCADE)
  name=models.CharField(max_length=150,null=False,blank=False)
  shop_name=models.CharField(max_length=150,null=False,blank=False)
  product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
  type=models.CharField(max_length=150,null=False,blank=False)
  price=models.FloatField(null=False,blank=False)
  quantity=models.IntegerField(null=False,blank=False)
  trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  created_at=models.DateTimeField(auto_now_add=True)
  
 
  def __str__(self):
    return self.name
  
class Cart(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  product_qty=models.IntegerField(null=False,blank=False)
  created_at=models.DateTimeField(auto_now_add=True)


  @property
  def total_cost(self):
    return self.product_qty*self.product.price
 
class Favourite(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)