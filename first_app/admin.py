from django.contrib import admin
from .models import *
# Register your models here.

class homeContentadmin(admin.ModelAdmin):
  list_display = ['head','headContent1','headContent2','headContent3','headContent4','headImg']
admin.site.register(homeInfo,homeContentadmin)


class homesliderforadmin(admin.ModelAdmin):
  list_display = ['head','headImg','header','city','paragraph']
admin.site.register(homeslider,homesliderforadmin)


class homelatestnewsforadmin(admin.ModelAdmin):
  list_display = ['header','headImg','date','paragraph']
admin.site.register(homelatestnews,homelatestnewsforadmin)


class homeclientsforadmin(admin.ModelAdmin):
  list_display = ['headImg1','headImg2','headImg3','headImg4','headImg5','headImg6']
admin.site.register(homeclients,homeclientsforadmin)


class aboutContentadmin(admin.ModelAdmin):
  list_display = ['head','headContent1','headContent2','headContent3','headContent4','headImg']
admin.site.register(aboutInfo,aboutContentadmin)

class aboutcreativeteamforadmin(admin.ModelAdmin):
  list_display = ['heading','teamsvideo','paragraph']
admin.site.register(aboutcreativeteam,aboutcreativeteamforadmin)


class Serviceformadmin(admin.ModelAdmin):
  list_display = ['img', 'header','content']
admin.site.register(ServiceData,Serviceformadmin)


class servicepricingplanforadmin(admin.ModelAdmin):
  list_display = ['text1','text2','text3','text4','text5','text6','text7']
admin.site.register(servicepricingplan,servicepricingplanforadmin)


class servicetextplanforadmin(admin.ModelAdmin):
  list_display = ['header1', 'textplan']
admin.site.register(servicetextplan,servicetextplanforadmin)  


class portgalleryphotoforadmin(admin.ModelAdmin):
  list_display = ['galleryImg']
admin.site.register(portphotogallery,portgalleryphotoforadmin)



class portgalleryvideoforadmin(admin.ModelAdmin):
  list_display = ['column1','galleryvideosImg','column2']
admin.site.register(portvideogallery,portgalleryvideoforadmin)

class portdemoadmin(admin.ModelAdmin):
  list_display = ['col1','gallerydemo']
admin.site.register(portdemo,portdemoadmin)

class portdemoadmin1(admin.ModelAdmin):
  list_display = ['col','gallerydemo1','row']
admin.site.register(portdemo1,portdemoadmin1)

class portdemoadmin2(admin.ModelAdmin):
  list_display = ['col','gallerydemo1','row']
admin.site.register(portdemo2,portdemoadmin2)

class Bookingforadmin(admin.ModelAdmin):
  list_display = ['name','email','number','totalamount','amount','order_id','paid','razorpay_payment_id']
admin.site.register(Booking,Bookingforadmin)  

class contactformadmin(admin.ModelAdmin):
  list_display = ['name','email','number','service','msg']
admin.site.register(contactform,contactformadmin)

class commentformadmin(admin.ModelAdmin):
  list_display = ['name','email','date','msg']
admin.site.register(commentform,commentformadmin)


class ceremonyBookforadmin(admin.ModelAdmin):
  list_display = ['name','email','number','fromDate','toDate']
admin.site.register(ceremonyBook,ceremonyBookforadmin)

class Items_detailsforadmin(admin.ModelAdmin):
  list_display = ["header","content","packageText1","packageText2","packageText3","packageText4","packageText5","packageText6","packageText7","img","img1","img2","img3","img4"]
admin.site.register(Items_details,Items_detailsforadmin) 
# admin.site.register(contactform)


class UserProfileforadmin(admin.ModelAdmin):
  list_display = ['user','fname','lname','bio','email','birthdate','contact','gender','address']
admin.site.register(UserProfile,UserProfileforadmin)  