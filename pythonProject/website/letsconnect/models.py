from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class homepics(models.Model):
    md = models.CharField(max_length=100)
    sd = models.TextField()
    img = models.ImageField(upload_to='pictures')
    textcolor = models.CharField(max_length=100)
    bordercolor = models.CharField(max_length=100)

class Userprofile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number=models.IntegerField()
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=200)
    address=models.TextField(max_length=100)
    About_you=models.TextField(max_length=150)
    pimage=models.ImageField()


