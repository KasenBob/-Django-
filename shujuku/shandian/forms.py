from django import forms

class RegisterForm(forms.Form):
    user_num = forms.CharField(label="用户名", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    account = forms.CharField(label="账号", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    shop_num = forms.CharField(label="商店编号", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))

class GoodForm(forms.Form):
	good_name = forms.CharField(label="商品名称", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
	good_num = forms.CharField(label="商品编号", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
	shop_num = forms.CharField(label="商店编号", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
	quantity = forms.CharField(label="数量", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
	created_time = forms.DateTimeField(label="生产日期", widget=forms.TextInput(attrs={'class': 'form-control'}))
	end_time = forms.DateTimeField(label="过期日期", widget=forms.TextInput(attrs={'class': 'form-control'}))
	fac_num = forms.CharField(label="工厂编号", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
	in_price = forms.IntegerField(label="进货价", widget=forms.TextInput(attrs={'class': 'form-control'}))
	out_price = forms.IntegerField(label="售价", widget=forms.TextInput(attrs={'class': 'form-control'}))

class FacForm(forms.Form):
	fac_num = forms.CharField(label="厂家编号", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
	fac_name = forms.CharField(label="厂家名称", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
	fac_position = forms.CharField(label="厂家位置", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
	fac_phone_num = forms.CharField(label="厂家联系方式", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))

class SaleForm(forms.Form):
	good_num = forms.CharField(label="商品编号", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
	shop_num = forms.CharField(label="商店编号", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
	sales_num = forms.CharField(label="数量", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))