import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.apps import apps


# RPG game main page
class RpgView(LoginRequiredMixin, ListView):
    model = apps.get_model('characters', 'Character')
    template_name = 'rpg/rpg_main.html'

    # Return only user data
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


# RPG combat view
class RpgBattleView(LoginRequiredMixin, DetailView):
    model = apps.get_model('characters', 'Character')
    template_name = 'rpg/rpg_battle.html'

    # Return only user data
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    # Call the Enemy class, and return random object from it
    def get_context_data(self, **kwargs):
        context = super(RpgBattleView, self).get_context_data(**kwargs)
        context['enemy'] = (apps.get_model('characters', 'Enemy')).objects.all()[random.randint(0, 6)]
        return context


# RPG instructions view
class RpgInstructionsView(LoginRequiredMixin, TemplateView):
    template_name = 'rpg/rpg_instructions.html'


