from django.shortcuts import render, redirect,render_to_response,get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
from django.conf import settings
from . import models
from .forms import RegisterForm,GoodForm,FacForm,SaleForm
from django.shortcuts import render,redirect

def index(request):
    pass
    return render(request,'login/index.html')
 
def login(request):
    if request.session.get('is_login',None):
        return redirect('/index')

    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        if username and password:  
            username = username.strip()
            try:
                user = models.User_info.objects.get(user_num=username)
                if user.password == password:
                    request.session['is_login'] = True
                    #print(user.shop_num)
                    request.session['shop_num'] = user.shop_num.shop_num
                    request.session['user_num'] = user.user_num
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'login/login.html', {"message": message})
    return render(request, 'login/login.html')
 
def register(request):
    if request.session.get('is_login', None):
        return redirect("/index/")

    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            user_num = register_form.cleaned_data['user_num']
            account = register_form.cleaned_data['account']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            shop_num = register_form.cleaned_data['shop_num']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User_info.objects.filter(user_num=user_num)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_acc_user = models.User_info.objects.filter(account=account)
                if same_acc_user:  # 用户名唯一
                    message = '账号已经存在，请重新选择账号！'
                    return render(request, 'login/register.html', locals())
                # 当一切都OK的情况下，创建新用户
 
                new_user = models.User_info.objects.create()
                new_user.user_num = user_num
                new_user.account = account
                new_user.password = password1
                new_user.shop_num = models.Shop_info.objects.get(shop_num=shop_num)
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())
 
def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/index/")
    request.session.flush()
    return redirect("/login/")

def goods_list(request):
    shopnum = request.session.get('shop_num', None)
    goods_all_list = models.Good_info.objects.filter(shop_num=shopnum)
    context = {}
    context['goods_list'] = goods_all_list
    return render(request, 'login/goods_list.html',context)

def facs_list(request):
    facs_all_list = models.facturer_info.objects.all()
    #print(facs_all_list)
    context = {}
    context['facs_list'] = facs_all_list
    return render(request, 'login/facs_list.html',context)

def sales_list(request):
    shopnum = request.session.get('shop_num', None)
    print(shopnum)
    shop = models.Shop_info.objects.get(shop_num=shopnum)
    print(type(shop))
    sales_all_list = models.Sales_records.objects.filter(shop_num=shop)
    print(sales_all_list)
    context = {}
    context['sales_lists'] = sales_all_list
    return render(request, 'login/sales.html',context)

def add_good(request):
    if request.method == "POST":
        good_form = GoodForm(request.POST)
        message = "请检查填写的内容！"
        if good_form.is_valid():  # 获取数据
            good_name = good_form.cleaned_data['good_name']
            good_num = good_form.cleaned_data['good_num']
            shop_num = good_form.cleaned_data['shop_num']
            quantity = good_form.cleaned_data['quantity']
            created_time = good_form.cleaned_data['created_time']
            end_time = good_form.cleaned_data['end_time']
            fac_num = good_form.cleaned_data['fac_num']
            in_price = good_form.cleaned_data['in_price']
            out_price = good_form.cleaned_data['out_price']
            same_num_good = models.Good_info.objects.filter(good_num=good_num)
            if same_num_good: 
                message = '商品编号已经存在，请重新输入商品编号！'
                return render(request, 'login/add_good.html', locals())
            new_good = models.Good_info.objects.create()
            new_good.good_name = good_name
            new_good.good_num = good_num
            new_good.shop_num = models.Shop_info.objects.get(shop_num=shop_num)
            new_good.quantity = int(quantity)
            new_good.created_time = created_time
            new_good.end_time = end_time
            new_good.fac_num = models.facturer_info.objects.get(fac_num=fac_num)
            new_good.in_price = in_price
            new_good.out_price = out_price
            new_good.save()
            return redirect('/goods_list/')  
    good_form = GoodForm()
    return render(request, 'login/add_good.html', locals())

def edit_good(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        good = models.Good_info.objects.filter(pk=nid).first()
        context = {}
        context['good'] = good
        return render(request, 'login/edit_good.html', context)
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        good_name = request.POST.get('good_name')
        good_num = request.POST.get('good_num')
        shop_num = request.POST.get('shop_num')
        quantity = request.POST.get('quantity')
        created_time = request.POST.get('created_time')
        end_time = request.POST.get('end_time')
        fac_num = request.POST.get('fac_num')
        in_price = request.POST.get('in_price')
        out_price = request.POST.get('out_price')
        pre_good = models.Good_info.objects.get(pk=nid)
        pre_good.good_name = good_name
        pre_good.good_num = good_num
        print(shop_num)
        pre_good.shop_num = models.Shop_info.objects.get(shop_num=shop_num)
        pre_good.quantity = quantity
        pre_good.created_time = created_time
        pre_good.end_time = end_time
        pre_good.fac_num = models.facturer_info.objects.get(fac_num=fac_num)
        pre_good.in_price = in_price
        pre_good.out_price = out_price
        pre_good.save()
        return redirect('/goods_list/')

def del_good(request):
    nid = request.GET.get('nid')
    models.Good_info.objects.filter(pk=nid).delete()
    return redirect('/goods_list/')

def add_fac(request):
    if request.method == "POST":
        fac_form = FacForm(request.POST)
        message = "请检查填写的内容！"
        if fac_form.is_valid():  # 获取数据
            fac_num = fac_form.cleaned_data['fac_num']
            fac_name = fac_form.cleaned_data['fac_name']
            fac_position = fac_form.cleaned_data['fac_position']
            fac_phone_num = fac_form.cleaned_data['fac_phone_num']
            same_num_fac = models.facturer_info.objects.filter(fac_num=fac_num)
            if same_num_fac: 
                message = '商品编号已经存在，请重新输入商品编号！'
                return render(request, 'login/add_fac.html', locals())
            new_fac = models.facturer_info.objects.create()
            new_fac.fac_num = fac_num
            new_fac.fac_name = fac_name
            new_fac.fac_position = fac_position
            new_fac.fac_phone_num = fac_phone_num
            new_fac.save()
            return redirect('/facs_list/')  
    fac_form = FacForm()
    return render(request, 'login/add_fac.html', locals())


def edit_fac(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        fac = models.facturer_info.objects.filter(pk=nid).first()
        context = {}
        context['fac'] = fac
        return render(request, 'login/edit_fac.html', context)
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        fac_num = request.POST.get('fac_num')
        fac_name = request.POST.get('fac_name')
        fac_position = request.POST.get('fac_position')
        fac_phone_num = request.POST.get('fac_phone_num')    
        pre_fac = models.facturer_info.objects.get(pk=nid)
        pre_fac.fac_num = fac_num
        pre_fac.fac_name = fac_name
        pre_fac.fac_position = fac_position
        pre_fac.fac_phone_num = fac_phone_num
        pre_fac.save()
        return redirect('/facs_list/')

def del_fac(request):
    nid = request.GET.get('nid')
    models.facturer_info.objects.filter(pk=nid).delete()
    return redirect('/facs_list/')

def add_sale(request):
    if request.method == "POST":
        sale_form = SaleForm(request.POST)
        message = "请检查填写的内容！"
        if sale_form.is_valid():  # 获取数据
            good_num = sale_form.cleaned_data['good_num']
            shop_num = sale_form.cleaned_data['shop_num']
            sales_num = sale_form.cleaned_data['sales_num']

            #算利润
            good = models.Good_info.objects.filter(good_num=good_num).first()
            #good_data = good._meta.fields
            #print(type(good))
            money = (int)(good.out_price - good.in_price)*(int)(sales_num)
            print(sales_num)
            print(money)
            #更新库存
            pre_good = models.Good_info.objects.get(good_num=good_num)
            pre_good.quantity = (int)(pre_good.quantity) - (int)(sales_num)
            pre_good.save() 

            new_sale = models.Sales_records.objects.create()
            new_sale.good_num = models.Good_info.objects.get(good_num=good_num)
            new_sale.shop_num = models.Shop_info.objects.get(shop_num=shop_num)
            new_sale.sales_num = (int)(sales_num)
            new_sale.profit = (int)(money)
            new_sale.save()
            return redirect('/sales/')  
    sale_form = SaleForm()
    return render(request, 'login/add_sale.html', locals())