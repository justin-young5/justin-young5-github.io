
from django import forms
from .models import Type, Entry
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
 
# create a ModelForm
class EntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))
    # specify the name of model to use
    class Meta:
        model = Entry
        fields = "__all__"