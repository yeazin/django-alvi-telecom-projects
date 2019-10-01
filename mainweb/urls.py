
#default views of mainweb app



from django.urls import path
from . import views


#app_name = "mainweb"

urlpatterns = [
    path('', views.home, name ="home"),
    path('all_user',views.user_type, name = 'all-user' ),
    path('user/<int:id>',views.usershow, name = 'single-user'),
    path( 'upcomming/', views.upcomming_product, name = 'products-comming' ),
    path('upcomming_product/<int:id>/', views.comming_product, name = 'single-up-product')



    #path('userinfo/', views.user_info, name ='user_info'),
    #path('userinfo/' ,views.user_type, name='usertype'),
    #path('products/',views.productshow,name = 'productspage'),
    #path('<int:id>', views.product_single, name='single_product'),
    #path('<int:id>', views.usershow, name ='user_show_now'),

]

