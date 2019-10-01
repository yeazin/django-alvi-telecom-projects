from django.db import models
#from django.core.validators import MaxValueValidator
from multiselectfield import MultiSelectField

# Create your models here.

# class of user information for many purposes



class User_information (models.Model):
    user_id = models.CharField(unique=True,
    blank=False,
    primary_key=False,
    serialize=True,
    max_length= 8,
    help_text='put the unique id number of user' )
    user_first_name = models.CharField(max_length=100, blank=False)
    user_last_name = models.CharField(max_length=100, blank=True)
    user_phone_num = models.CharField(blank=False, max_length=11, help_text ='put valid Bangladesh Number')
    user_address = models.TextField(blank=True,max_length=1000000)
    user_email=models.EmailField(blank=True)
    user_benifits =(
        ('can print in low rate','can print in low rate'),
        ('can have extra commission in photocopy','can have extra commsision in photcopy'),
        ('can make argument',' can make argument')
    )
    what_benifits =MultiSelectField(choices=user_benifits, max_length = 1000, max_choices = None, blank= True)
    activity_status = models.BooleanField(default=False,help_text='If the user is active check the box')
    user_photo=models.ImageField( blank=True,upload_to='user_photo',null=True,)
    #user_join_date=models.DateTimeField(auto_now=False)

    def __str__(self):
        return  self.user_first_name



#catagory of products

class Product_catagory(models.Model):
    catagory_name = models.CharField(max_length=500, )

    def __str__(self):
        return self.catagory_name


# class of products
# admin panel model

class Products(models.Model):
    image=models.ImageField(upload_to='static/media/products',blank=True)
    product_id=models.CharField(max_length=5,blank=False,unique=True)
    product_title = models.CharField(max_length=200, blank=False)
    product_price= models.IntegerField()
    #product_price_discount=models.IntegerField()
    product_description = models.TextField(max_length=None)

    def short_description(self):
        return self.product_description[:100]

    def __str__(self):
        return self.product_title


#class of new launch of products

class Products_Launch(models.Model):
    launch_date = models.DateTimeField(auto_now=False)
    product_name = models.CharField(max_length= 1000,blank=False)
    product_catagory = models.ForeignKey(Product_catagory, on_delete=models.CASCADE,null=True)
    product_description = models.TextField()
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to = 'products_launch', blank = True, null = True )
    condition = [
        ('New','New'),
        ('Used','Used')
    ]
    product_condition = models.CharField(max_length=10, choices = condition)

    def short_description(self):
        return self.product_description [:100]

    def __str__(self):
        return self.product_name

























