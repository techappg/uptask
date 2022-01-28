from django import forms

from django.core.exceptions import ValidationError

from taskapp.models import *
from projectapp.models import *



class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        # fields = '__all__'
        fields=("first_name","last_name","username","email","phone_number","office_user_id","reporting_to","programming_language")

    # def validate_mail(value):
    #     if "@gmail.com" in value:
    #         return value
    #     else:
    #         raise ValidationError("This field accepts mail id of google only")


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    #
class ProgrammingLanguageForm(forms.ModelForm):

    class Meta:
        model=ProgrammingLanguage
        fields=("language_name",)
    #

    def clean_language_name(self):
        language_name = self.cleaned_data.get('language_name')
        if ProgrammingLanguage.objects.filter(language_name=language_name).exists():
            raise forms.ValidationError("Language name already exists")
        return language_name

class TaskTypeForm(forms.ModelForm):

     class Meta:
         model= TaskType
         fields=("type_name","programming_language","for_all")




class  SystemDetailForm(forms.ModelForm):
     class Meta:
         model= system_detail
         fields=("system_type","specification","system_service","system_id","added_on")

         def system_id(self):
             system_id = self.cleaned_data.get('system_id')
             print(system_id)
             if system_detail.objects.filter(system_id=system_id).exists():
                 raise forms.ValidationError("System already exists")
             return system_id

class SystemAssignedDetailForm(forms.ModelForm):
    class Meta:
        model=Assigned_System_Detail
        fields=("system_id","user","assigned_type","assigned_on","returned_on",)


class ViewUserTaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=("user","task_type","details")

class ViewUserProjectForm(forms.ModelForm):
    class Meta:
        model= Project
        fields=('user', 'title', 'details', 'is_active', 'completed', 'started', 'started_on', 'completed_on','id')

