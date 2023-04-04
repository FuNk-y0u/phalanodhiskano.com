from django import forms

class CreateList(forms.Form):
    name = forms.CharField(label="Your List Title", max_length = 200)
    by_name = forms.CharField(label="Your Name", max_length = 200)
    check = forms.BooleanField(required = False)

