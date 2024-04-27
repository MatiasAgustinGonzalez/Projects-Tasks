from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Lider, Sponsor, Tarjeta


def home_view(request):
    return render(request, "Projects/home.html")

# -----------------------------------------------------------------------------
# --------------------------------   CRUD   -----------------------------------
# -----------------------------------------------------------------------------

class TarjetaListView(ListView):
    model = Tarjeta
    template_name = "Projects/cards/list_cards.html"
    context_object_name = "TARJETAS_LIST"

class TarjetaCreateView(CreateView):
    model = Tarjeta
    template_name = "Projects/cards/form_create_cards.html"
    fields = ['lider', 'sponsor', 'titulo', 'descripcion', 'fecha_inicio', 'fecha_fin','estado']
    success_url = reverse_lazy("list_cards")

class FilterBySponsorListView(ListView):
    model = Tarjeta
    template_name = "Projects/cards/filter_cards.html"
    context_object_name = "TARJETAS_FILTER"

    def get_queryset(self):
        sponsor_name = self.kwargs['sponsor_name']
        return Tarjeta.objects.filter(sponsor__nombre=sponsor_name)

class FilterByLiderListView(ListView):
    model = Tarjeta
    template_name = "Projects/cards/filter_cards.html"
    context_object_name = "TARJETAS_FILTER"

    def get_queryset(self):
        lider_name = self.kwargs['lider_name']
        return Tarjeta.objects.filter(lider__nombre=lider_name)
