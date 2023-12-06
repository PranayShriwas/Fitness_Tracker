# tracker_app/urls.py
from django.urls import path
from .views import home, log_workout, set_goal

urlpatterns = [
    path('', home, name='home'),
    path('log_workout/', log_workout, name='log_workout'),
    path('set_goal/', set_goal, name='set_goal'),
]
