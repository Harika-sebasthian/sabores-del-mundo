from django import forms

class ConsultaForm(forms.Form):
    nombre = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ej: María García',
            'id': 'nombre',
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ej: maria@email.com',
            'id': 'email',
        })
    )
    asunto = forms.ChoiceField(
        choices=[
            ('', 'Seleccioná un motivo'),
            ('Reserva', 'Reservar una mesa'),
            ('Evento privado', 'Evento privado'),
            ('Consulta del menú', 'Consulta sobre el menú'),
            ('trabajo', 'Trabaja con nosotros'),
            ('Otro', 'Otro'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-input form-select',
            'id': 'asunto',
        })
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-input form-textarea',
            'placeholder': 'Contanos tu consulta, fecha, cantidad de personas...',
            'rows': 5,
            'id': 'mensaje',
        })
    )