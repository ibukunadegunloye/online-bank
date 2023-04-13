from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from .models import ExtendedUser



class ExtendedUserForm(forms.ModelForm):

    phone_number = forms.CharField(label="Phone Number", widget=forms.TextInput(attrs={'placeholder': '+234XXXXXXXXXX'}))

    class Meta:
        model = ExtendedUser
        fields = [
            'email',
            'first_name',
            'last_name',
            'country',
            'phone_number',
            'address',
            'gender',
            'occupation',
            'date_of_birth',
        ]
        widgets = {
            'country': CountrySelectWidget(),
            'date_of_birth': forms.widgets.DateTimeInput(attrs={'type': 'date'}),
        }
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    pin = forms.CharField(min_length=6, max_length=6, widget=forms.PasswordInput)
    confirm_pin = forms.CharField(max_length=6, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        pin = cleaned_data.get("pin")
        confirm_pin = cleaned_data.get("confirm_pin")

        if not pin.isdigit():
            raise forms.ValidationError("PINs must be only digits")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        if int(pin) != int(confirm_pin):
            raise forms.ValidationError("PINs do not match")

        if len(pin) != 6:
            raise forms.ValidationError('PIN must be 6 characters long.')


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.pin = self.cleaned_data['pin']
        if commit:
            user.save()
        return user




class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
     