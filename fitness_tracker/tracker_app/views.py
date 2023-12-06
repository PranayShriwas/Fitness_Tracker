# tracker_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Exercise, Workout, Goal
from django.contrib import messages
from django.http import HttpResponse

@login_required
def home(request):
    workouts = Workout.objects.filter(user=request.user)
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'home.html', {'workouts': workouts, 'goals': goals})

@login_required
def log_workout(request):
    if request.method == 'POST':
        exercise_id = request.POST.get('exercise')
        duration = request.POST.get('duration')
        date = request.POST.get('date')

        try:
            exercise = Exercise.objects.get(id=exercise_id)
        except Exercise.DoesNotExist:
            return HttpResponse("Invalid Exercise")

        Workout.objects.create(user=request.user, exercise=exercise, duration=duration, date=date)
        messages.success(request, 'Workout logged successfully!')
        return redirect('home')

    exercises = Exercise.objects.all()
    return render(request, 'log_workout.html', {'exercises': exercises})

@login_required
def set_goal(request):
    if request.method == 'POST':
        target_weight = request.POST.get('target_weight')

        goal, created = Goal.objects.update_or_create(user=request.user, defaults={'target_weight': target_weight})
        messages.success(request, 'Goal set successfully!')
        return redirect('home')

    return render(request, 'set_goal.html')
