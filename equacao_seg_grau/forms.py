from django import forms
from .models import Equacao2Grau


# Existem dois tipos de formularios no django
# modelForm -- acoplado aos dados

class Equacao2GrauForm(forms.ModelForm):
    class Meta:
        model = Equacao2Grau
        fields = ['a', 'b', 'c']
        

# form.Form --> desacoplado dos dados