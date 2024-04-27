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

#--------------------------------
#   LISTAR todos los registros
#--------------------------------

class TarjetaListView(ListView):
    model = Tarjeta
    template_name = "Projects/cards/list_cards.html"
    context_object_name = "TARJETAS_LIST"

class FilterBySponsorListView(ListView):
    model = Tarjeta
    template_name = "Projects/cards/filter_cards.html"
    context_object_name = "TARJETAS_FILTER"

    def get_queryset(self):
        sponsor_name = self.kwargs['sponsor_name']
        return Tarjeta.objects.filter(sponsor__nombre=sponsor_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sponsor_name = self.kwargs['sponsor_name']
        context['filtro_tipo'] = f'Sponsor ({sponsor_name})'
        return context

class FilterByLiderListView(ListView):
    model = Tarjeta
    template_name = "Projects/cards/filter_cards.html"
    context_object_name = "TARJETAS_FILTER"

    def get_queryset(self):
        lider_name = self.kwargs['lider_name']
        return Tarjeta.objects.filter(lider__nombre=lider_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lider_name = self.kwargs['lider_name']
        context['filtro_tipo'] = f'Líder ({lider_name})'
        return context


#--------------------------------
#   CREAR todos los registros
#--------------------------------

class TarjetaCreateView(CreateView):
    model = Tarjeta
    template_name = "Projects/cards/form_create_cards.html"
    fields = ['lider', 'sponsor', 'titulo', 'descripcion', 'fecha_inicio', 'fecha_fin','estado']
    success_url = reverse_lazy("list_cards")

class LiderCreateView(CreateView):
    model = Lider
    template_name = "Projects/cards/form_create_lider.html"
    fields = ['nombre']
    success_url = reverse_lazy("list_cards")

class SponsorCreateView(CreateView):
    model = Sponsor
    template_name = "Projects/cards/form_create_sponsor.html"
    fields = ['nombre']
    success_url = reverse_lazy("list_cards")


#--------------------------------
#   LEER todos los registros
#--------------------------------

class TarjetaDetailView(DetailView):
    model = Tarjeta
    template_name = "Projects/cards/detail_cards.html"
    context_object_name = "TARJETAS"


#--------------------------------
# ACTUALIZAR todos los registros
#--------------------------------



#--------------------------------
#   BORRAR todos los registros
#--------------------------------

class TarjetaDeleteView(DeleteView):
    model = Tarjeta
    template_name = "Projects/cards/form_delete_cards.html"
    success_url = reverse_lazy("list_cards")

