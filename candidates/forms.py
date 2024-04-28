from django import forms

class CandidateForm(forms.Form):
  name = forms.CharField(label="姓名", max_length=100)
  party = forms.CharField(label="政黨", max_length=50)
  age = forms.IntegerField(label="年齡")