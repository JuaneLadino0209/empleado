from django import forms

class NewDepartamentoForm(forms.Form):
    name = forms.CharField(max_length= 50)
    last_name = forms.CharField(max_length= 50)
    departament = forms.CharField(max_length= 50)
    shorname = forms.CharField(max_length= 20)

    