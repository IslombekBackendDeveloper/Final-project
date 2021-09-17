from django import forms
from django.db import models
from django.db.models import fields
from .models import Profile, Skill


class ProfileUpdateForm(forms.ModelForm):
    class Meta:

        model = Profile
        fields = '__all__'

class NewSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill']
