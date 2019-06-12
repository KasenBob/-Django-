from django.contrib import admin
from .models import *

@admin.register(Shop_info)
class Shop_info_Admin(admin.ModelAdmin):
	list_display=('shop_num','shop_position','shop_phone_num')

@admin.register(Good_info)
class Good_info_Admin(admin.ModelAdmin):
	list_display=('good_name','good_num','shop_num','quantity','created_time','end_time','fac_num','in_price','out_price')

@admin.register(Sales_records)
class Sales_records_Admin(admin.ModelAdmin):
	list_display=('shop_num','good_num','profit')

@admin.register(facturer_info)
class Shop_info_Admin(admin.ModelAdmin):
	list_display=('fac_num','fac_name','fac_position','fac_phone_num')

@admin.register(User_info)
class Shop_info_Admin(admin.ModelAdmin):
	list_display=('user_num','account','password','shop_num')
