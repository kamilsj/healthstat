from django import forms
from django_countries.widgets import CountrySelectWidget
from .models import UserProfile, HealthData
from django.utils.translation import gettext as _


class UsersForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profilephoto','height', 'bday', 'gender', 'country']
        labels = {
            'profilephoto': _('Your profile photo'),
            'height': _('Height'),
            'bday': _('Birthday'),
            'gender': _('Gender'),
            'country': _('Country')
        }
        widgets = {
            'bday': forms.DateInput(attrs={'type': 'date'}),
            'country': CountrySelectWidget(),

        }


class HealthDataForm(forms.ModelForm):
    class Meta:
        model = HealthData
        fields = ['weight', 'neck', 'waist', 'hip']
