from django.forms import ModelForm
from .models import Post
from django.apps import apps


# Journal entry form
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['character', 'title', 'text']

    # Filter only user characters
    def __init__(self, user, *args, **kwargs):
        model = apps.get_model('characters', 'Character')
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['character'].queryset = model.objects.filter(user=user)
        self.fields['text'].label = "Write your tale here"