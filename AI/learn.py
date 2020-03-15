from . import ml
import math


class CalcuclateChanges:
    
    def __init__(self):
        pass
        
    def WeightChanges(weight):
        
        x = 1
        
        while x != 0:    
            for weigthData in weight:
                pass
        

class WeightCalculations:

    def __init__(self):
        pass

    def WeightIdeal(self, gender, height):
        ratio = (height - 152.4)/2.54
        if gender == 0:
            delta = 1.41*ratio
            weight = 56.2+delta
        else:
            delta = 1.36*ratio
            weight = 53.1+delta

        bmi = weight / (height / 100) ** 2
        result = [weight, bmi]

        return result



    def BodyFatIdeal(self, gender, age):
        result = 0
        if gender==0:
            if 20 <= age < 30:
                result = 8.5
            elif 25 <= age < 30:
                result = 10.5
            elif 30 <= age < 35:
                result = 12.7
            elif 35 <= age < 40:
                result = 13.7
            elif 40 <= age < 45:
                result = 15.3
            elif 45 <= age < 50:
                result = 16.4
            elif 50 <= age < 55:
                result = 18.9
            elif age >= 55:
                result = 20.9
        else:
            if 20 <= age < 30:
                result = 17.7
            elif 25 <= age < 30:
                result = 18.4
            elif 30 <= age < 35:
                result = 19.3
            elif 35 <= age < 40:
                result = 21.5
            elif 40 <= age < 45:
                result = 22.2
            elif 45 <= age < 50:
                result = 22.9
            elif 50 <= age < 55:
                result = 25.2
            elif age >= 55:
                result = 26.3

        return result



    def BodyFat(self, gender, neck, hip, waist, height):

        if gender == 0:
            result = (495/(1.0324 - 0.19077*math.log(waist-neck, 10)+0.15456*math.log(height, 10))) - 450
        else:
            result = (495/(1.29579 - 0.35004*math.log(waist+hip-neck, 10) + 0.22100*math.log(height, 10))) - 450

        return result