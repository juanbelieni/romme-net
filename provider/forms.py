from django import forms


class ProviderForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=200)
    phone = forms.CharField(label="Telefone", max_length=15)
    address = forms.CharField(label="Endereço", max_length=200)

    # Handle Bootstrap forms
    def __init__(self, *args, **kwargs):
        super(ProviderForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-3'
