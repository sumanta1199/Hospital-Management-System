import email
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class doctor(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phno=models.IntegerField()
    pwd=models.CharField(max_length=50)
    edu=models.CharField(max_length=50)
    spe=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    class Meta:
        db_table="doctor"
        
class patient(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phno=models.IntegerField()
    pwd=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    blood_group=models.CharField(max_length=50)
    class Meta:
        db_table="patient"
        
class booking(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phno=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
    fees=models.IntegerField()
    class Meta:
        db_table="booking"
        
class docupdate(models.Model):
     name=models.CharField(max_length=50)
     pre=models.CharField(max_length=5000)
     class Meta:
         db_table="docupdate"
    
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()
    image = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.title + " by " + self.author

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username

class contact(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    email=models.EmailField()
    query=models.CharField(max_length=1000)
    city=models.CharField(max_length=50)
    pre=models.ImageField(upload_to='contact/images', default="")
