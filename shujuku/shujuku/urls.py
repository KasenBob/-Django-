"""shujuku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shandian import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('sales/', views.sales_list),
    path('goods_list/', views.goods_list),
    path('add_good/',views.add_good),
    path('edit_good/',views.edit_good),
    path('del_good/',views.del_good),
    path('facs_list/', views.facs_list),
    path('add_fac/',views.add_fac),
    path('edit_fac/',views.edit_fac),
    path('del_fac/',views.del_fac),
    path('add_sale/',views.add_sale),
]


