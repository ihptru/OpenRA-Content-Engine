from django import forms

class UploadMapForm(forms.Form):
    info    = forms.CharField(max_length=400)
    file    = forms.FileField()
