from apps.forum.models import Forum
from apps.forum.forms import ForumForm
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, DetailView, ListView)

class ForumCreateView(CreateView):
    model = Forum
    template_name = "forum/create_forum.html"
    form_class = ForumForm


class ForumUpdateView(UpdateView):
    model = Forum
    template_name = "forum/update_forum.html"
    form_class = ForumForm


class ForumDeleteView(DeleteView):
    model = Forum
    template_name = "forum/delete_forum.html"
    success_url = "/"  # Rediriger vers l'URL souhaitée après la suppression


class ForumDetailView(DetailView):
    model = Forum
    template_name = "forum/detail_forum.html"


class ForumListView(ListView):
    model = Forum
    template_name = "forum/list_forum.html"
