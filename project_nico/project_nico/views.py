from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps


# Index page
class HomePage(TemplateView):
    template_name = 'index.html'


# About page
class AboutView(TemplateView):
    template_name = 'about.html'


# Profile page
class ProfilePage(LoginRequiredMixin, ListView):
    template_name = 'profile.html'
    model = apps.get_model('characters', 'Character')

    # Show only user data
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
