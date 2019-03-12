from django import forms
from .models import Account, Service, FixService, Cart, Payment, Report


class Login(forms.ModelForm):
    class Meta:
        model = Account
        fields = {'username', 'password', }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'username', 'placeholder': 'Tên đăng nhập...'}),
            'password': forms.TextInput(attrs={'class': 'password', 'placeholder': 'Mật khẩu...', 'type': 'password'})
        }


class Signup(forms.ModelForm):
    class Meta:
        model = Account

        fields = {'username', 'password', 'sex', 'email', 'phone', }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'username1', 'placeholder': 'Tên đăng nhập...'}),
            'password': forms.TextInput(attrs={'class': 'password1', 'placeholder': 'Mật khẩu...', 'type': 'password'}),
            'email': forms.TextInput(attrs={'class': 'email1', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'phone1', 'placeholder': 'Số điện thoại...'}),
            'sex': forms.Select(attrs={'class': 'sex1'})
        }


class UpdateAccount(forms.ModelForm):
    class Meta:
        model = Account

        fields = {'username', 'address', 'email', 'phone', 'password', }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'username1', 'placeholder': 'Tên đăng nhập...'}),
            'password': forms.TextInput(attrs={'class': 'password1', 'placeholder': 'Mật khẩu...', 'type': 'password'}),
            'email': forms.TextInput(attrs={'class': 'email1', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'phone1', 'placeholder': 'Số điện thoại...'}),
            'address': forms.TextInput(attrs={'class': 'address1', 'placeholder': 'Địa chỉ ...'}),
        }


class ServiceRegister(forms.ModelForm):
    class Meta:
        model = Service

        fields = {'customer_name', 'address', 'phone',}
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'username1', 'placeholder': 'Tên đăng nhập...'}),
            'address': forms.TextInput(attrs={'class': 'address1', 'placeholder': 'Địa chỉ...'}),
            'phone': forms.TextInput(attrs={'class': 'phone1', 'placeholder': 'Số điện thoại...'}),
        }


class ServiceAssign(forms.ModelForm):
    class Meta:
        model = FixService

        fields = {'product', 'fix', 'error', 'is_guarantee', 'employee', }


class Carts(forms.ModelForm):
    class Meta:
        model = Cart
        fields = {'product', 'user', 'number'}
    number = forms.TextInput(attrs={'class': 'number_cart'}),


class Pay(forms.ModelForm):
    class Meta:
        model = Payment
        fields = {'payment', }


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report

        fields = {'fixed', 'assignee', 'type_report', 'is_fixed', }
