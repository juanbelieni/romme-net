from django import forms
from .models import MaterialCategory


class MaterialForm(forms.Form):

    name = forms.CharField(label="Nome", max_length=200)
    category = forms.ChoiceField(choices=MaterialCategory.choices)

    # Handle Bootstrap forms
    def __init__(self, *args, **kwargs):
        super(MaterialForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control mb-3"
