from django.db import models


class AnalyseData(models.Model):
    usrId = models.BigIntegerField(blank=False)