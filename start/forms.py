from django import forms
from django_countries.widgets import CountrySelectWidget
from .models import UserProfile, HealthData


class UsersForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profilephoto','height', 'bday', 'gender', 'country']
        widgets = {
            'bday': forms.DateInput(attrs={'type': 'date'}),
            'country': CountrySelectWidget(),

        }


class HealthDataForm(forms.ModelForm):
    class Meta:
        model = HealthData
        fields = ['weight', 'neck', 'waist', 'hip']
