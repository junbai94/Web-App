from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=128)
    
class SpotForm(forms.Form):
    spotID = forms.CharField(label='Input spotID', max_length=128)
    date = forms.DateField(label = 'Select date', widget=forms.SelectDateWidget)
    
class FutForm(forms.Form):
    instID = forms.CharField(label='Future tick symbol', max_length=10)
    date = forms.DateField(label = 'Select date', widget=forms.SelectDateWidget)
    
class UploadForm(forms.Form):
    ID = forms.IntegerField()
    misc = forms.CharField()