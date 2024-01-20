from typing import Any
from django import forms
from app.models import *

class Topicform(forms.Form):
    Topic_name=forms.CharField()

def validate_for_a(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('cannot starts with a')
    

def length(data):
    if len(data)<5:
        raise forms.ValidationError('cannot give 5 characters')

class WebPageform(forms.Form):
    tl=[[to.Topic_name,to.Topic_name] for to in Topic.objects.all()]
    Topic_name=forms.ChoiceField(choices=tl)
    name=forms.CharField(validators=[validate_for_a,length])
    url=forms.URLField()
    Email=forms.EmailField()
    Recreateemail=forms.EmailField()
    botcatcher=forms.CharField(required=False, widget=forms.HiddenInput)

    
    def clean(self):
        e=self.cleaned_data['Email']
        r=self.cleaned_data['Recreateemail']
        if e!=r:
            raise forms.ValidationError('valid email')
    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('bot')
     