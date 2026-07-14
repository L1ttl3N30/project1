from django import forms


class bffForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
#    description = forms.CharField(label='Description', widget=forms.Textarea)
    questions = forms.CharField(label='Questions', widget=forms.Textarea)