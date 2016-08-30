from django import forms
from django.forms import ModelForm
# from dateutil.relativedelta import relativedelta
from datetime import timedelta, date
from django.utils import timezone
from django.forms.widgets import SelectDateWidget
from django.utils.translation import ugettext_lazy as _

from todoist.models import Task
from django.contrib.auth.models import User

# class RegistrationForm(ModelForm):
# 	password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))

# 	class Meta:
# 		model = User
# 		fields = ['username', 'email']

class RegistrationForm(forms.Form):

    username = forms.RegexField(regex=r'^\w+$', \
    	widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), \
            error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True,\
    	max_length=30)), label=_("Email address"))
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True,\
    	max_length=30, render_value=False)), label=_("Password"))


class TaskForm(ModelForm):
    current_year = timezone.now().year
    deadline_date = forms.DateField(
                    widget=SelectDateWidget(\
                            years=[y for y in range(current_year,current_year + 1)]),
                    label=_("Date"))
    class Meta:
        model = Task
        fields = ['name']
        widgets = {
                'name': forms.TextInput(attrs={'required':'True'},\
                    # error_messages={'invalid': _("This value must contain only letters, numbers and underscores.")}\
                    ),
                }
