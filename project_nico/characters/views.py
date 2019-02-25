from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CreateCharacterForm
from .models import Character
from django.urls import reverse_lazy


# Character creation View
class CreateCharacterView(LoginRequiredMixin, CreateView):
    form_class = CreateCharacterForm
    success_url = reverse_lazy('characters:list')
    template_name = 'characters/character_form.html'

    # Binds character to the user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Characters list View
class CharactersListView(LoginRequiredMixin, ListView):
    template_name = 'characters/character_list.html'
    model = Character

    # Show user info only
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


# Character update View
class CharacterEditView(LoginRequiredMixin, UpdateView):
    model = Character
    form_class = CreateCharacterForm
    success_url = reverse_lazy('characters:list')

    # Show user info only
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

# Character Delete View
class CharacterDeleteView(LoginRequiredMixin, DeleteView):
    model = Character
    success_url = reverse_lazy('characters:list')

    # Show user info only
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)