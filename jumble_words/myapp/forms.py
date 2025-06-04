from django import forms

class PlayerInfoForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50)
    age = forms.IntegerField(label="Age", min_value=1)
    place = forms.CharField(label="Place", max_length=50)

class GuessForm(forms.Form):
    guess = forms.CharField(label="Your guess", max_length=50)
