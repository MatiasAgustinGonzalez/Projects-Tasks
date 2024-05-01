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
from .forms import TarjetaSearchForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


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

class LiderListView(ListView):
    model = Lider
    template_name = "Projects/master/list_detail_lider.html"
    context_object_name = "LIST_DETAIL_LIDER"

class SponsorListView(ListView):
    model = Sponsor
    template_name = "Projects/master/list_detail_sponsor.html"
    context_object_name = "LIST_DETAIL_SPONSOR"

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
    template_name = "Projects/master/form_create_lider.html"
    fields = ['nombre']
    success_url = reverse_lazy("list_lider")

class SponsorCreateView(CreateView):
    model = Sponsor
    template_name = "Projects/master/form_create_sponsor.html"
    fields = ['nombre']
    success_url = reverse_lazy("list_cards")


#--------------------------------
#   LEER todos los registros
#--------------------------------

class TarjetaDetailView(DetailView):
    model = Tarjeta
    template_name = "Projects/cards/detail_cards.html"
    context_object_name = "TARJETAS"

def tarjeta_search_view(request):
    if request.method == "GET":
        form = TarjetaSearchForm()
        return render(request, "Projects/cards/form_search_cards.html", context={"SEARCH_FORM": form})
    elif request.method == "POST":
        form = TarjetaSearchForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data["titulo"]
            estado = form.cleaned_data["estado"]
            tarjetas_encontradas = Tarjeta.objects.filter(titulo__icontains = titulo)
            if estado:
                tarjetas_encontradas = tarjetas_encontradas.filter(estado = estado)
            contexto_dict = {"TARJETAS_LIST": tarjetas_encontradas}
            return render(request, "Projects/cards/list_cards.html", context=contexto_dict)
    else:
        return render(request,"Projects/cards/form_search_cards.html", context = {"SEARCH_FORM": form} )


#--------------------------------
# ACTUALIZAR todos los registros
#--------------------------------

class TarjetaUpdateView(UpdateView):
    model = Tarjeta
    template_name = "Projects/cards/edit_cards.html"
    context_object_name = "TARJETAS"
    fields = ["lider", "sponsor", "titulo", "descripcion", "fecha_inicio", "fecha_fin", "estado"]
    success_url = reverse_lazy("list_cards")

class LiderUpdateView(UpdateView):
    model = Lider
    template_name = "Projects/master/edit_lider.html"
    context_object_name = "LIDER"
    fields = ["nombre"]
    success_url = reverse_lazy("list_lider")

class SponsorUpdateView(UpdateView):
    model = Sponsor
    template_name = "Projects/master/edit_sponsor.html"
    context_object_name = "SPONSOR"
    fields = ["nombre"]
    success_url = reverse_lazy("list_sponsor")


#--------------------------------
#   BORRAR todos los registros
#--------------------------------

class TarjetaDeleteView(DeleteView):
    model = Tarjeta
    template_name = "Projects/cards/form_delete_cards.html"
    context_object_name = "TARJETAS"
    success_url = reverse_lazy("list_cards")

class LiderDeleteView(DeleteView):
    model = Lider
    template_name = "Projects/master/form_delete_lider.html"
    context_object_name = "LIDER"
    success_url = reverse_lazy("list_lider")

class SponsorDeleteView(DeleteView):
    model = Sponsor
    template_name = "Projects/master/form_delete_sponsor.html"
    context_object_name = "SPONSOR"
    success_url = reverse_lazy("list_sponsor")


# -----------------------------------------------------------------------------
# --------------------------   LOGIN LOGOUT   ---------------------------------
# -----------------------------------------------------------------------------

#--------------------------------
#             LOGIN
#--------------------------------

def user_login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.user_cache
            if user is not None:
                login(request, user)
                return redirect("home")

    return render(request, "Projects/profile/login.html", {"FORM_LOGIN": form})


#--------------------------------
#             LOGOUT
#--------------------------------

def user_logout_view(request):
    logout(request)
    return redirect("login")