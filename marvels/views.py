from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Marvels

class MarvelsListView(ListView):
    template_name = "pages/marvels_list.html"
    model = Marvels


class MarvelsDetailView(DetailView):
    template_name = "pages/marvels_detail.html"
    model = Marvels


class MarvelsCreateView(CreateView):
    template_name = "pages/marvels_create.html"
    model = Marvels
    fields = ['name', 'description', 'owner']


class MarvelsUpdateView(UpdateView):
    template_name = "pages/marvels_update.html"
    model = Marvels
    fields = ['name', 'description', 'owner']


class MarvelsDeleteView(DeleteView):
    template_name = "pages/marvels_delete.html"
    model = Marvels
    success_url = reverse_lazy("marvels_list")