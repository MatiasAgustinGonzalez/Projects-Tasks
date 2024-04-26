from django.shortcuts import render, redirect
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