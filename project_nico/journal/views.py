from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView,  ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from .models import Post


#Journal main view
class JournalMainView(LoginRequiredMixin, ListView):
    template_name = 'journal/journal_main.html'

    # This is to check if there are characters created
    # Returns a list and check if true in template
    model = apps.get_model('characters', 'Character')

    # Show only user data
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


# Journal entry creation view
@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.user, request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('journal:entries')
    else:
        form = PostForm(request.user)
    return render(request, 'journal/post_form.html', {'form': form})


# Posts list view
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 50

    # Show only user data
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


# Post selected view
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

    # Show only user data
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


# Journal entry update View
class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text']
    success_url = reverse_lazy('journal:entries')

    # Show user info only
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


# Journal entry Delete View
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('journal:entries')

    # Show user info only
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)