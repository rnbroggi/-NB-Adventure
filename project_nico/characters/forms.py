from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Character


class CreateCharacterForm(ModelForm):
    class Meta:
        model = Character
        error_css_class = 'error'
        fields = ['name', 'race', 'gender', 'char_class', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Name"
        self.fields['race'].label = "Race"
        self.fields['gender'].label = "Gender"
        self.fields['char_class'].label = "Class"
        self.fields['description'].label = "Description (optional)"

    def clean_name(self):
        name = self.cleaned_data['name']
        chars = set('0123456789$,!@#$%^&*()_+=-`}{:"?><~/.;[]')
        for char in chars:
            if char in name:
                raise ValidationError('Name should not contain any numbers or symbols!')
        if ' ' in name:
            raise ValidationError('Name should not contain any spaces!')
        return name

