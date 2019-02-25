from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserCreateForm(UserCreationForm):

    class Meta:

        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def clean(self):
        cleaned_data = super().clean()