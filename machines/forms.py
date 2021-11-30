from django import forms


class MachinesForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=200)
    description = forms.CharField(label="Descrição", max_length=300)

    # Handle Bootstrap forms
    def __init__(self, *args, **kwargs):
        super(MachinesForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-3'