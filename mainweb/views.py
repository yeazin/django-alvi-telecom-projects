from django.shortcuts import render,get_object_or_404
from .models import User_information,Products,Products_Launch
#from django.core.urlresolvers import reverse



# Create your views here.

def home(request):
    return render (request,'index.html')


def upcomming_product(request):
    product = Products_Launch.objects.all()
    context = {
        'product':product
    }
    return render (request, 'launch.html',context)


#function about showing one launing product by row

def comming_product (request ,id ):
    product = get_object_or_404(Products_Launch, pk=id )

    context = {
        "product":product
    }
    return render (request, 'upcomming_single.html', context)

#to show all user at once

def user_type(request):
    information = User_information.objects.all()
    context = {
        "information":information
    }
    return render (request, 'userinfo.html' ,context )


# for sigle user information view

def usershow(request, id):
    #passing the value of one particuler object
    #usersingle = User_information.objects.get(pk = user_id)
    usersingle = get_object_or_404(User_information, pk=id)
    context = {
        "usersingle": usersingle
    }
    return render (request, 'singleuser.html', context)






'''

#for the request of all user id number
def user_type(request):
    information = User_information.objects.all()
    context : {
        "information":information
    }
    return render (request, 'userinfo.html' ,context )
def productshow(request):
    products=Products.objects.all()
    context : {
        "products":products
    }
    return render (request, 'products.html', context)

#function is made for showing single product on line

def product_single(request, id):
    product = get_object_or_404(Products,pk=id)
    context : {
    'product':product
    }
    return render (request, 'single_product.html', context )



# for sigle user information view

def usershow(request, id):
    #passing the value of one particuler object
    #usersingle = User_information.objects.get(pk = user_id)
    usersingle = get_object_or_404(User_information, pk=id)
    context = {
        "usersingle": usersingle
    }
    return render (request, 'singleuser.html', context)
'''
