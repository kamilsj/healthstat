from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from .forms import UsersForm, HealthDataForm
from .models import UserProfile, HealthData, ApiTokens
from datetime import datetime, date, timedelta
from AI.learn import WeightCalculations
from modules.groups.strava import *
from modules.importer import ImportStravaDataApi


class Index(View):

    form_class = HealthDataForm

    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            usrId = user.id
            data = {
                'date': datetime.today()
            }
            if not HealthData.objects.filter(usrId=usrId).filter(date__startswith=date.today()).exists():
                form = self.form_class
                data['added'] = 1
            else:
                form = {}
                data['added'] = 0

        return render(request, 'start.html', {'form': form, 'data': data})

    def post(self, request):
        if request.method == 'POST':
            user = request.user
            usrId = user.id
            form = self.form_class(request.POST)
            if form.is_valid():
                user_profile = UserProfile.objects.get(usrId=usrId)
                if user_profile.height > 0 and user_profile.height <= 250:
                    bmi = form.cleaned_data['weight']/(user_profile.height/100)**2 #FORMULA FOR BMI
                else:
                    bmi = 0
                obj = form.save(commit=False)
                obj.bmi = bmi
                obj.usrId = user.id
                obj.save()

        return redirect('/')


def activities(request):
    from bokeh.io import output_notebook
    
    data = {}
    
    
    return render(request, 'start/activities.html', {'data': data})

class ImportActivities(View):

    def get(self, request):
        data = {}
        strava = 0
        strava_url = ''
        code = request.GET.get('code')
        if code:
            strava = StravaToken(code=code)
        else:
            strava_url = StravaUrl()

        if strava and strava != 0:
            athlete = strava.get_athlete()
            activities = strava.get_activities()
            imported = ImportStravaDataApi()
            for activity in activities:
                print(activity.moving_time)
                imported.AddApi(request.user.id, activities)

            data = {
                'athlete': athlete.firstname,
                
            }

        return render(request, 'start/import_activities.html', {
            'data': data,
            'strava_url': strava_url
        })


    def post(self, request):
        pass


def profile(request, profile_id=0):
    user = request.user
    calculations = WeightCalculations()
    if profile_id and profile_id != 0:
        profile = User.objects.get(id=profile_id)
        detailed_profile = UserProfile.objects.get(usrId=profile_id)
        detailed_body = HealthData.objects.filter(neck__gte=1,
                                                  hip__gte=1,
                                                  waist__gte=1,
                                                  usrId=profile_id).last()
    else:
        profile = User.objects.get(id=user.id)
        detailed_profile = UserProfile.objects.get(usrId=user.id)
        detailed_body = HealthData.objects.filter(neck__gte=1,
                                                  hip__gte=1,
                                                  waist__gte=1,
                                                  usrId=user.id).last()

    age = (date.today() - detailed_profile.bday) // timedelta(days=365.2425)
    IdealWeight = calculations.WeightIdeal(detailed_profile.gender, detailed_profile.height)
    BodyFat = calculations.BodyFat(detailed_profile.gender, detailed_body.neck,
                                   detailed_body.hip, detailed_body.waist, detailed_profile.height)
    data = {
        'name': profile.get_full_name(),
        'id': user.id,
        'age': age,
        'IdealWeight': IdealWeight,
        'BodyFat': BodyFat,
    }

    return render(request, 'profile.html', {'data': data})


class UpdateProfile(View):
    form_class = UsersForm
    calculations = WeightCalculations()
    def get(self, request):
        init_data = UserProfile.objects.get(usrId=request.user.id)
        form = self.form_class(initial={'height': init_data.height, 'bday': init_data.bday,
                                        'gender': init_data.gender, 'country': init_data.country})
        return render(request, 'update_profile.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            user = request.user
            form = self.form_class(request.POST)
            if form.is_valid():
                if UserProfile.objects.filter(usrId=user.id).exists():
                    UserProfile.objects.filter(usrId=user.id).update(
                        height = form.cleaned_data.get('height'),
                        gender = form.cleaned_data.get('gender'),
                        bday = form.cleaned_data.get('bday'),
                        country = form.cleaned_data.get('country'),
                    )

                else:
                    obj = form.save(commit=False)
                    obj.idealweight = self.calculations.WeightIdeal(form.cleaned_data.get('gender'), form.cleaned_data.get('height'))[0]
                    obj.usrId = user.id
                    obj.save()
                return redirect('/start/profile/')
            else:
                return redirect('/start/profile/update')


def q(request):
    if request.method == 'GET':
        q = request.GET['q']

        result = {}
        return render(request, 'searchresult.html', {'result': result, 'q': q})
    else:
        return None