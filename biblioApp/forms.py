from django import forms

class FormularioContactos(forms.Form):
    asunto = forms.CharField(max_length=100, min_length=4)
    email = forms.EmailField(required=False)
    mensaje = forms.CharField(widget=forms.Textarea)
