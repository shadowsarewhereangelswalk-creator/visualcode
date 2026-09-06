from datetime import date

from django import forms

from .models import Reserva


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ["nombre", "correo", "servicio", "fecha", "mensaje"]
        widgets = {"fecha": forms.DateInput(attrs={"type": "date"}), "mensaje": forms.Textarea(attrs={"rows": 4})}

    def clean_fecha(self):
        fecha = self.cleaned_data["fecha"]
        if fecha < date.today():
            raise forms.ValidationError("Selecciona una fecha futura.")
        return fecha

