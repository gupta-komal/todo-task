from datetime import timedelta, date
from django.utils import timezone
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django import forms
from django.views.generic import View

from todoist.models import Task
from todoist.forms import TaskForm
from todoist.views.user_views import get_tasks_for_user


class TaskView(LoginRequiredMixin, View):

    def get(self, request):
        form = TaskForm(initial={'deadline_date':date.today()})

        return render_to_response('todoist/create_task.html',\
            {'form':form}, context_instance=RequestContext(request))

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task.objects.create( \
                     name = form.cleaned_data['name'], \
                     status = "not_done", \
                     user = request.user, \
                     deadline_date = form.cleaned_data['deadline_date'] \
                    )
            date_chosen = form.cleaned_data['deadline_date']

            return redirect('/tasks/'+str(date_chosen))


class EditTaskView(LoginRequiredMixin, View):

    def get(self, request, task_id):
        task = Task.objects.get(id=int(task_id))
        date = task.deadline_date
        form = TaskForm(instance=task,initial={'deadline_date':date})

        return render_to_response('todoist/edit_task.html',\
                {'form':form, 'task_id':str(task_id)}, \
                context_instance=RequestContext(request))

    def post(self, request, task_id):
        form = TaskForm(request.POST)
        if form.is_valid():
            task_name = form.cleaned_data['name']
            task_date = form.cleaned_data['deadline_date']
            Task.objects.filter(id=task_id)\
                    .update(name=task_name,\
                    deadline_date=task_date, status="not_done")

            return redirect('/tasks/'+str(task_date))


@login_required
def get_tasks_for_date(request, task_date):
    user_tasks = get_tasks_for_user(request.user)
    tasks = user_tasks.filter(deadline_date=task_date)

    return render_to_response('todoist/view_tasks_for_date.html',\
            {'tasks':tasks}, \
            context_instance=RequestContext(request))

@login_required
def mark_task_done(request,task_id):
    Task.objects.filter(id=task_id).update(status="done")

    return redirect('/home/')
