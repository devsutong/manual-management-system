from django.db import models


import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File

import random


# Create your models here.
class Item(models.Model):
    brand_name: models.CharField(max_length=512)
    model_name = models.CharField(max_length=512)
    manufacturer= models.CharField(max_length=512)
    manual = models.FileField(upload_to ='manuals/')
    drawing = models.FileField(upload_to ='drawings/')
    qrcode = models.ImageField(upload_to="qrcodes/")

    def save(self,*args,**kwargs):
      qrcode_img=qrcode.make(self.url)
      canvas=Image.new("RGB", (300,300),"white")
      draw=ImageDraw.Draw(canvas)
      canvas.paste(qrcode_img)
      buffer=BytesIO()
      canvas.save(buffer,"PNG")
      self.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
      canvas.close()
      super().save(*args,**kwargs)
    
