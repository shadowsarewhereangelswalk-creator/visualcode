from django import forms

from .models import Solicitud


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ["servicio", "nombre", "correo", "mensaje"]
        widgets = {"mensaje": forms.Textarea(attrs={"rows": 5})}

    def clean_mensaje(self):
        mensaje = self.cleaned_data["mensaje"].strip()
        if len(mensaje) < 15:
            raise forms.ValidationError("Describe tu proyecto con al menos 15 caracteres.")
        return mensaje

