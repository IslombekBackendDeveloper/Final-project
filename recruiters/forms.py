from django.forms import ModelForm
from django import forms
from .models import Job


class NewJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        help_texts = {
            'skills_req': 'Enter all the skills required each separated by commas.',
            'link': 'If you want candidates to apply on your company website rather than on our website, please provide the link where candidates can apply. Otherwise, please leave it blank or candidates would not be able to apply directly!',
        }


class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        help_texts = {
            'skills_req': 'Enter all the skills required each separated by commas.',
            'link': 'If you want candidates to apply on your company website rather than on our website, please provide the link where candidates can apply. Otherwise, please leave it blank or candidates would not be able to apply directly!',
        }