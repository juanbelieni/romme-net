from django import forms


class ServiceForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=200)

    # Handle Bootstrap forms
    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control mb-3"
