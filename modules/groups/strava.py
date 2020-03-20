from stravalib import Client
from modules.secrets import STRAVA_DATA
from start.models import ApiTokens

strava_data = STRAVA_DATA


def CheckApiTokens(usrId):
    if ApiTokens.objects.filter(usrId=usrId).exist():
        pass


def StravaUrl(client_id=strava_data[0], redirect_url='http://127.0.0.1:8000/start/activities/import'):
    client = Client()
    url = client.authorization_url(client_id=client_id, redirect_uri=redirect_url)

    return url


def StravaToken(client_id=strava_data[0], client_secret=strava_data[1], code=''):
    client = Client()
    access = client.exchange_code_for_token(client_id=client_id, client_secret=client_secret, code=code)
    client.access_token = access['access_token']
    client.refresh_token = access['refresh_token']
    expires_at = access['expires_at']

    return client

