from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
#from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.views import login
from django.contrib.auth import logout
from django import forms
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from todoist.models import Task
from todoist.forms import RegistrationForm, TaskForm

# Create your views here.

def index(request):
    registration_form = RegistrationForm()
    login_form = AuthenticationForm()
    return render_to_response('registration/index.html',\
            {'registration_form':registration_form, 'login_form':login_form},\
            context_instance = RequestContext(request))


def custom_login(request):
    if request.user.is_authenticated():

        return redirect('/home')
    else:

        return login(request)

class RegisterView(View):

    def get(self, request):

        return HttpResponseRedirect('/')

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                    username = form.cleaned_data['username'],
                    email = form.cleaned_data['email'],
                    password = form.cleaned_data['password']
                    )

            return HttpResponseRedirect('/register/success')
        else:
            HttpResponseRedirect('/')


def registration_success(request):
    return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

#can be moved to UserProfile
def get_tasks_for_user(user):
    return Task.objects.filter(user=user, status="not_done")

#also be moved to UserProfile
def get_next_7_days_tasks(user):
    tasks_for_next_7_days = []
    present_date = timezone.now().date()
    duration_period = timedelta(days=7)
    user_tasks = get_tasks_for_user(user)

    date = timezone.now().date()
    while date-present_date < duration_period:
        date += timedelta(days=1)
        tasks_for_the_day = user_tasks.filter(deadline_date=date)
        tasks_dic_for_date = {'tasks': tasks_for_the_day, 'date': date}
        tasks_for_next_7_days.append(tasks_dic_for_date)

    return tasks_for_next_7_days

@login_required
def get_my_tasks(request):
    tasks_for_next_7_days = get_next_7_days_tasks(request.user)

    return render_to_response('todoist/home.html', \
            {'tasks_for_next_7_days':tasks_for_next_7_days},
            context_instance=RequestContext(request))
