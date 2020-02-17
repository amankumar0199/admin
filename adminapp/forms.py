from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from adminapp.models import institude,Student,teacher,type,CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.core import validators
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email','password1','password2')


#this is the form for type registration
class choiceRegisterForm(forms.ModelForm):
    class Meta:
        model = type #model name of choice
        fields = ('choice','phone_no','pincode') #fields describe in type model

    def clean(self):
        total_cleaned_data = super().clean()
        inputphone = total_cleaned_data['phone_no']
        if str(inputphone)[0] != "9" or len(str(inputphone)) != 10:
            raise forms.ValidationError('Write Phone No. to be correct !!')


#this is the form for institude registration
class institudeRegisterForm(forms.ModelForm):
    class Meta:
        model = institude #model name of institude
        fields = ('institude_name',) #fields describe in institude model

#this is the form for teacher registration
class teacherRegisterForm(forms.ModelForm):
    class Meta:
        model = teacher #model name of teacher
        fields = ('first_name','last_name') #fields describe in teacher model

#this is the form for Student registration
class studentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student #model name of Student
        fields = ('first_name','last_name','school_name') #fields describe in student model
