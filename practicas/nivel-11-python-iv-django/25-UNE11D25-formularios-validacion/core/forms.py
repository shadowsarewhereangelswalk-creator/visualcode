from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(min_length=2, max_length=80)
    correo = forms.EmailField()
    asunto = forms.ChoiceField(choices=[("proyecto", "Proyecto"), ("mentoria", "Mentoría"), ("otro", "Otro")])
    mensaje = forms.CharField(min_length=15, max_length=1000, widget=forms.Textarea(attrs={"rows": 5}))
    aceptar = forms.BooleanField()

    def clean_correo(self):
        correo = self.cleaned_data["correo"].strip().lower()
        if correo.endswith("@example.com"):
            raise forms.ValidationError("Utiliza un correo real.")
        return correo

    def clean(self):
        datos = super().clean()
        if datos.get("asunto") == "proyecto" and len(datos.get("mensaje", "")) < 30:
            self.add_error("mensaje", "Describe el proyecto con al menos 30 caracteres.")
        return datos

