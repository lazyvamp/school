from django.contrib.auth.forms import UserCreationForm
from django.db import models
from core.models import BaseUser
from django.core.exceptions import ValidationError
 
 
class UserSignUpForm(UserCreationForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if BaseUser.objects.filter(email=email).exists():
            raise ValidationError("email already exists")
        else:
            return email

    def clean_username(self):
        username = self.cleaned_data['username']
        
        if BaseUser.objects.filter(username=username).exists():
            raise ValidationError("username already exists")
        else:
            return username
    
    def clean_phone_no(self):
        phone_number = self.cleaned_data['phone_number']
        
        if BaseUser.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("account with phone already exists")
        else:
            return phone_number

    class Meta:
        model = BaseUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'phone_number', 'role')
    
