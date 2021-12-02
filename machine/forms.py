from django import forms


class MachineForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=200)
    description = forms.CharField(label="Descrição", max_length=300, widget=forms.Textarea)

    # Handle Bootstrap forms
    def __init__(self, *args, **kwargs):
        super(MachineForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-3'