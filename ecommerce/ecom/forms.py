from django import forms
from django.contrib.auth.models import User
from . import models


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput(),
        
        }
        


# from django import forms
# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError

# class CustomerUserForm(forms.ModelForm):
#     confirm_password = forms.CharField(
#         label="Confirm Password",
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#         required=True
#     )

#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'password']  # Exclude confirm_password here

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password and confirm_password and password != confirm_password:
#             raise forms.ValidationError("Passwords do not match.")

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user





class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile','profile_pic']

class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['name','price','description','product_image']





