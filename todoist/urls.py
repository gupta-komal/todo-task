from django.conf.urls import url, include
from todoist.views.user_views import custom_login, index, RegisterView, registration_success, \
        logout_view, get_my_tasks
from todoist.views.task_views import TaskView, EditTaskView,\
        get_tasks_for_date, mark_task_done


urlpatterns = [
    url(r'register/success/$', registration_success, name='registration_success'),
    url(r'register/$', RegisterView.as_view(), name='register'),
    url(r'^$', index, name='index'),
    url(r'^accounts/login/', index),
    url(r'^login/$', 'django.contrib.auth.views.login', name='django_login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^home/$', get_my_tasks, name='home'),
    url(r'^task/create/$', TaskView.as_view(), name='create_task'),
    url(r'^task/(?P<task_id>[0-9]+)/edit/$', EditTaskView.as_view(), name='edit_task'),
    url(r'^tasks/(?P<task_date>[-\w]+)$', get_tasks_for_date, name='get_tasks_for_date'),
    url(r'^task/(?P<task_id>[0-9]+)/mark_done/$', mark_task_done, name='mark_task_done')
]
