from django import forms
from .models import Register

class RegisterForm(forms.ModelForm):
	class Meta:
		model = Register
		fields = '__all__'
		