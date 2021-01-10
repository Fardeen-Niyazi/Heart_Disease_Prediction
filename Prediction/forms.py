from django import forms
from .import models

class Predict_Form(forms.ModelForm):
    class Meta:
        model = models.Predictions
        fields = ('age','sex','cp','resting_bp','serum_cholesterol','fasting_blood_sugar','resting_ecg','max_heart_rate',
        'exercise_induced_angina','st_depression','st_slope','number_of_vessels','thallium_scan_results')
        widgets = {'age': forms.TextInput(attrs={'class': 'form-control'}),
                   'sex': forms.Select(attrs={'class': 'form-control'}),
                   'cp': forms.Select(attrs={'class': 'form-control'}),
                   'resting_bp':forms.TextInput(attrs={'class': 'form-control'}),
                   'serum_cholesterol':forms.TextInput(attrs={'class': 'form-control'}),
                   'fasting_blood_sugar':forms.Select(attrs={'class': 'form-control'}),
                   'resting_ecg':forms.Select(attrs={'class': 'form-control'}),
                   'max_heart_rate':forms.TextInput(attrs={'class': 'form-control'}),
                   'exercise_induced_angina':forms.Select(attrs={'class': 'form-control'}),
                   'st_depression':forms.TextInput(attrs={'class': 'form-control'}),
                   'st_slope':forms.Select(attrs={'class': 'form-control'}),
                   'number_of_vessels':forms.Select(attrs={'class': 'form-control'}),
                   'thallium_scan_results':forms.Select(attrs={'class': 'form-control'}),
                   }

from .models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter username'}
    ), required=True, max_length=50)

    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email Id'}
    ), required=True, max_length=50)

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter password'}
    ), required=True, max_length=50)

    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm password'}
    ), required=True, max_length=50)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm password does not match"
            )


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('profile_pic',)


