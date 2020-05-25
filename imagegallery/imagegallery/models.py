from django.db import models

class imggal(models.Model):
    imgtitle=modelsCharField(max_length=100)
    imgdesc=modelsCharField(max_length=500)
    image=models.ImageField(upload_to='images/')
