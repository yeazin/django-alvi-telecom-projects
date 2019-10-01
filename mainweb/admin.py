from django.contrib import admin
from .models import User_information,Products,Products_Launch,Product_catagory


# Register your models here.
admin.site.site_header= 'Alvi telecom dashboard'

# admin customization of User_information

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id','user_first_name','user_last_name','user_email','activity_status')
    list_filter = ('user_id',)
    search_fields=('user_id','user_first_name','user_email','user_phone_num')

admin.site.register(User_information, UserAdmin)

# admin customization of product_description

class ProductAdmin(admin.ModelAdmin):
    list_display= ('product_id','product_title','product_price')
    list_filter= ('product_title','product_id')
    search_fields= ('product_title','product_id','product_price')

admin.site.register(Products,ProductAdmin)


#admin customization of product launch

class Products_launchAdmin(admin.ModelAdmin):
    list_display = ( 'product_name','launch_date','product_price' ,'product_catagory','product_condition')
    list_filter = ('product_name',)
    search_fields = ('product_name','launch_date')

admin.site.register(Products_Launch, Products_launchAdmin)


admin.site.register(Product_catagory)

