from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Quiz
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email','password1','password2']
		 

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields =['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']				 

"""class UploadFileForm(forms.ModelForm):
	title = forms.CharField(max_length=50)
	file = forms.FileField()

	class Meta:
		model = Document	
		fields = ['file']	"""

class QuizUploadForm(forms.ModelForm):
	class Meta:
		model = Quiz
		fields = ['username', 'pdf']