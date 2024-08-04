from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class homeInfo(models.Model):
  head = models.CharField(max_length=100,null=True)
  headContent1 = models.TextField(max_length=1000,null=True)
  headContent2 = models.TextField(max_length=1000,null=True)
  headContent3 = models.TextField(max_length=1000,null=True)
  headContent4 = models.TextField(max_length=1000,null=True)
  headImg = models.ImageField(upload_to='images/',null=True)
  


class homeslider(models.Model):
    head = models.CharField(max_length=100,null=True)
    headImg = models.ImageField(upload_to='images/')
    header = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    paragraph =  models.CharField(max_length=2000,null=True)


class homelatestnews(models.Model):
     header = models.CharField(max_length=100,null=True) 
     headImg = models.ImageField(upload_to='images/') 
     date = models.DateField(max_length=100,null=True)
     paragraph =  models.CharField(max_length=500,null=True)


class homeclients(models.Model):
     headImg1 = models.ImageField(upload_to='images/')  
     headImg2 = models.ImageField(upload_to='images/')  
     headImg3 = models.ImageField(upload_to='images/')  
     headImg4 = models.ImageField(upload_to='images/')  
     headImg5 = models.ImageField(upload_to='images/')  
     headImg6 = models.ImageField(upload_to='images/') 


class aboutInfo(models.Model):
  head = models.CharField(max_length=100,null=True)
  headContent1 = models.TextField(max_length=1000,null=True)
  headContent2 = models.TextField(max_length=1000,null=True)
  headContent3 = models.TextField(max_length=1000,null=True)
  headContent4 = models.TextField(max_length=1000,null=True)
  headImg = models.ImageField(upload_to='images/',null=True) 

class aboutcreativeteam(models.Model):
   heading = models.CharField(max_length=100,null=True) 
   teamsvideo =  models.FileField(upload_to='videos/')  
   paragraph = models.CharField(max_length=100,null=True)   

 

class servicepricingplan(models.Model):
   text1 = models.CharField(max_length=100)  
   text2 = models.CharField(max_length=100)  
   text3 = models.CharField(max_length=100)  
   text4 = models.CharField(max_length=100)  
   text5 = models.CharField(max_length=100)  
   text6 = models.CharField(max_length=100)  
   text7 = models.CharField(max_length=100)  

class servicetextplan(models.Model):
   header1 = models.CharField(max_length=200)
   textplan = models.TextField()  

class portphotogallery(models.Model):
   galleryImg = models.ImageField(upload_to='images/')  

class portvideogallery(models.Model):
   column1 = models.CharField(max_length=100,null=True)   
   column2 = models.CharField(max_length=100,null=True) 
   galleryvideosImg = models.ImageField(upload_to='images/')

class portdemo(models.Model):
   col1 = models.CharField(max_length=100,null=True)   
   gallerydemo = models.ImageField(upload_to='images/')

class portdemo1(models.Model):
   row = models.CharField(max_length=100,null=True,default='')   
   gallerydemo1 = models.ImageField(upload_to='images/')
   col = models.CharField(max_length=100,null=True)  

class portdemo2(models.Model):
   row = models.CharField(max_length=100,null=True,default='')   
   gallerydemo1 = models.ImageField(upload_to='images/')
   col = models.CharField(max_length=100,null=True)  

class ServiceData(models.Model):
  header = models.CharField(max_length=100)
  img = models.ImageField(upload_to='images/')
  content = models.CharField(max_length=100) 


class Items_details(models.Model):
  header = models.CharField(max_length=100)
  content = models.CharField(max_length=100)
  img = models.ImageField(upload_to='images/')
  packageText1 = models.CharField(max_length=100, null=True)    
  packageText2 = models.CharField(max_length=100, null=True)    
  packageText3 = models.CharField(max_length=100, null=True)    
  packageText4 = models.CharField(max_length=100, null=True)    
  packageText5 = models.CharField(max_length=100, null=True)    
  packageText6 = models.CharField(max_length=100, null=True)    
  packageText7 = models.CharField(max_length=100, null=True)
  img1 = models.ImageField(upload_to='images/')    
  img2 = models.ImageField(upload_to='images/')    
  img3 = models.ImageField(upload_to='images/')    
  img4 = models.ImageField(upload_to='images/')    
     
class ceremonyBook(models.Model):
   name = models.CharField(max_length=100)
   email = models.CharField(max_length=100)
   number = models.CharField(max_length=50)
   fromDate = models.DateField(default=datetime.date.today)    
   toDate = models.DateField(default=datetime.date.today)    

class contactform(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length= 100)
  number = models.CharField(max_length=50)
  service = models.CharField(max_length=100)
  msg = models.TextField()


class commentform(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length= 100)
  date = models.DateTimeField(default=datetime.datetime.now,blank=True)
  msg = models.TextField()





class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    bio = models.TextField()
    email = models.EmailField()
    birthdate = models.DateField(blank=True, null=True)
    contact = models.CharField(max_length=10)
    gender = models.CharField(max_length=20)
    address = models.TextField()

    def str(self): 
        return f"{self.fname,self.lname,self.email}"



class Booking(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    number =models.CharField(max_length=10)
    email = models.EmailField()
    totalamount = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(default=0)
    order_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
 
    def __str__(self):
        if self.paid == True:
            return self.name + " paid"
        else:
            return self.name + " not paid"