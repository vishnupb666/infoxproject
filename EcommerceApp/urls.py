from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name='home'),
   path('log_in',views.log_in,name='log_in'),
   path('sign_up',views.sign_up,name='sign_up'),
   path('log_out',views.log_out,name='log_out'),
   path('viewprofile',views.viewprofile,name='viewprofile'),
   path('updateprofile',views.updateprofile,name='updateprofile'),
   path('addcategory',views.addcategory,name='addcategory'),
   path('admin_dash',views.admin_dash,name='admin_dash'),
   path('addproduct',views.addproduct,name='addproduct'),
   path('view_users',views.view_users,name='view_users'),
   path('listCategory',views.listCategory,name='listCategory'),
   path('listProduct',views.listProduct,name='listProduct'),
   path('searchProduct/<int:pk>',views.searchProd,name='searchProduct'),
   path('addkartView/<int:pk>',views.addkartView,name='addkartView'),
   path('viewKart/<int:pk>',views.viewKart,name='viewKart'),
]