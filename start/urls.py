from django.urls import path
from . import views
from . import detailed

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.UpdateProfile.as_view(), name='update profile'),
    path('profile/<int:profile_id>', views.profile, name="users profile"),
    path('activities/', views.activities, name='activities'),
    path('activities/import/', views.ImportActivities.as_view(), name='import activities'),
    path('q/', views.q, name='q'),
    path('detailed/', detailed.index, name='')
]