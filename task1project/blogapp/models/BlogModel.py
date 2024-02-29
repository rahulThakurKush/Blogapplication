from distutils.command.upload import upload
from django.db import models
class blogdata(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    blogimg = models.ImageField(upload_to="blogapp/image",default = "")
    