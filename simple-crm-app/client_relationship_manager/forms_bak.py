from django import forms
from .models import Client, Device
from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()#get our own custom user

class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Client       
        verbose_name = 'client'
        verbose_name_plural = 'clients'

        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            "address": forms.TextInput(attrs={'class': 'form-input'}),
        }


class UpdateClientForm(forms.ModelForm):
    class Meta:
        model = Client       
        verbose_name = 'client'
        verbose_name_plural = 'clients'

        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            "address": forms.TextInput(attrs={'class': 'form-input'}),
        }

class FaultyDeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
        
        fields = '__all__'
        widgets = {
            'name' :forms.TextInput(attrs={'class':'form-input'}),
            'serial':forms.TextInput(attrs={'class':'form-input'}),
            'siteName':forms.TextInput(attrs={'class':'form-input'}),
            'faultDescription':forms.Textarea(attrs={'class':'form-input'}),
            'technician':forms.TextInput(attrs={'class':'form-input'}),
            
        }
        

class CustomUserCreationForm(UserCreationForm):
     class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# class LoginForm(forms.Form):
#     email = forms.EmailField(
#         label='Your email',
#         widget=forms.EmailInput(
#             attrs={
#                 'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
#                 'placeholder': 'name@company.com',
#                 'required': True,
#             }
#         )
#     )
#     password = forms.CharField(
#         label='Password',
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
#                 'placeholder': '••••••••',
#                 'required': True,
#             }
#         )
#     )

