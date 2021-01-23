from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    content = models.TextField()
    image = models.ImageField(upload_to='pics',blank=True,null=True)
    categori = models.CharField(max_length=25)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)


