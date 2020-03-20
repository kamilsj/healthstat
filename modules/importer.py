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

                    if activity.id > 0:
                        activity_id = activity.id

                        if activity.name is not None:
                            name = str(activity.name)
                        else:
                            name = ''

                        if activity.distance is not None:
                            distance = float(activity.distance)
                        else:
                            distance = 0

                        if activity.moving_time is not None:
                            moving_time = str(activity.moving_time)
                        else:
                            moving_time = ''

                        if activity.elapsed_time is not None:
                            elapsed_time = str(activity.elapsed_time)
                        else:
                            elapsed_time = ''

                        if activity.total_elevation_gain is not None:
                            total_elevation_gain = str(activity.total_elevation_gain)
                        else:
                            total_elevation_gain = ''

                        if activity.average_speed is not None:
                            average_speed = float(activity.average_speed)
                        else:
                            average_speed = 0

                        if activity.max_speed is not None:
                            max_speed = float(activity.max_speed)
                        else:
                            max_speed = 0

                        if activity.average_temp is not None:
                            average_temp = float(activity.average_temp)
                        else:
                            average_temp = 0

                        if activity.average_cadence is not None:
                            average_cadence = float(activity.average_cadence)
                        else:
                            average_cadence = 0

                        if activity.average_watts is not None:
                            average_watts = float(activity.average_watts)
                        else:
                            average_watts = 0

                        if activity.elev_high is not None:
                            elev_high = float(activity.elev_high)
                        else:
                            elev_high = 0

                        if activity.elev_low is not None:
                            elev_low = float(activity.elev_low)
                        else:
                            elev_low = 0

                        if activity.calories is not None:
                            calories = float(activity.calories)
                        else:
                            calories = 0

                        ac = ActivitiesStravaData(
                            usrId=usrId,
                            activity_id=activity_id,
                            name=name,
                            distance=distance,
                            moving_time=moving_time,
                            elapsed_time=elapsed_time,
                            total_elevation_gain = total_elevation_gain,
                            average_speed=average_speed,
                            max_speed=max_speed,
                            average_temp=average_temp,
                            average_cadence=average_cadence,
                            average_watts=average_watts,
                            elev_high=elev_high,
                            elev_low=elev_low,
                            calories=calories

                        )
                        ac.save()
                else:
                    continue
        else:
            return False

    def CheckData(self, file):
        pass