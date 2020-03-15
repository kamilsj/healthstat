from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from start.models import HealthData, UserProfile
from datetime import datetime

from AI.learn import WeightCalculations, CalcuclateChanges


class ActivitieData(APIView):
    pass



class ChartData(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    calculations = WeightCalculations()
    

    def get(self, request):
        user = request.user
        health = HealthData.objects.filter(usrId=user.id).all().order_by('-id')[:10].values()
        label = []
        chartData = []
        weight = []
        if health.count() > 1:
            for healthData in health:
                label.append(healthData['date'].strftime("%d %b %y"))
                chartData.append(round(healthData['bmi'], 2))
                weight.append(healthData['weight'])
        else:
            label = health[0]['date'].strftime("%d %b %y")
            chartData = round(health[0]['bmi'], 2)
            weight = health[0]['weight']
            

        profile = UserProfile.objects.get(usrId=user.id)
        [IdealWeight, bmi] = self.calculations.WeightIdeal(profile.gender, profile.height)

        data = {
            'label': label,
            'chartData': chartData,
            'bmi': round(bmi, 2),
            'weight': weight,
            'idealweight': round(IdealWeight, 2)
        }

        return Response(data)

