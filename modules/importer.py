import csv
import fitparse
import tcxparser
from start.models import ActivitiesStravaData

class ImportStravaDataApi:

    def __init__(self):
        pass

    def AddApi(self, usrId, activities):
        if usrId > 0 and activities:
            for activity in activities:
                if not ActivitiesStravaData.objects.filter(activity_id=activity.id):

                    ac = ActivitiesStravaData(
                        usrId=usrId,
                        activity_id=activity.id,
                        name=activity.name,
                        distance=float(activity.distance),
                        moving_time=activity.moving_time,
                        elapsed_time=activity.elapsed_time,
                        average_speed=float(activity.average_speed),
                        max_speed=float(activity.max_speed),
                        average_temp=float(activity.average_temp),
                        average_cadence=float(activity.average_cadence),
                        average_watts=float(activity.average_watts),
                        elev_high=float(activity.elev_high),
                        elev_low=float(activity.elev_low),
                        #calories=float(activity.calories)

                    )
                    ac.save()
        else:
            return False

    def CheckData(self, file):
        pass