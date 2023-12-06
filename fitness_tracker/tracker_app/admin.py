from django.contrib import admin
from .models import Exercise,Goal,Workout
# Register your models here.
admin.site.register(Exercise)
admin.site.register(Goal)
admin.site.register(Workout)

