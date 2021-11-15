from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead, User, Agent

class LeadModelForm(forms.ModelForm):
	class Meta:
		model = Lead
		fields = (
			'first_name',
			'last_name',
			'age',
			'agent',
			)


class LeadForm(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()
	age = forms.IntegerField(min_value=0)

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("username",)
		field_classes = {'username' : UsernameField}

class AssignAgentForm(forms.Form):
	agent = forms.ModelChoiceField(queryset=Agent.objects.none())

	def __init__(self, *args, **kwargs):
		request = kwargs.pop("request")
		# print(request.user)
		agents = Agent.objects.filter(organisation=request.user.userprofile)
		super(AssignAgentForm, self).__init__(*args, **kwargs)
		self.fields["agent"].queryset = agents

	def form_valid(self, form):
		print(form.cleaned_data)
		return super(AssignAgentView, self).form_valid(form)

class LeadCategoryUpdate(forms.ModelForm):
	class Meta:
		model = Lead
		fields = (
			'category', 
		)