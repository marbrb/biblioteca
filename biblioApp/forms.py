from django import forms

class FormularioContactos(forms.Form):
    asunto = forms.CharField(max_length=100, min_length=4)
    email = forms.EmailField(required=False)
    mensaje = forms.CharField(widget=forms.Textarea)

    #Django busca automaticamente un metodo "clean_" y nombre del campo y ejecuta este durante la validacion.
    def clean_message(self):
        """funcion para validar que el comentario tenga almenos cuatro palabras"""
        message = self.cleaned_data['mensaje']  #diccionario de datosque se enviaron bien del form
        words = len(message.split())
        if words < 4:
            raise forms.ValidationError("¡Se requiere un mínimo de 4 palabras!")
        return message
