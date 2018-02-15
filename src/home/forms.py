from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
	
	class Meta:
		model = Registration
		fields = '__all__'
		template_name='home/register.html'
