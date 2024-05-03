from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from  django.contrib.auth.decorators import login_required
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
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .forms import UserEditForm



@login_required
def home_view(request):
    return render(request, "Projects/home.html")

# -----------------------------------------------------------------------------
# --------------------------------   CRUD   -----------------------------------
# -----------------------------------------------------------------------------

#--------------------------------
#   LISTAR todos los registros
#--------------------------------

class TarjetaListView(LoginRequiredMixin, ListView):
    model = Tarjeta
    template_name = "Projects/cards/list_cards.html"
    context_object_name = "TARJETAS_LIST"

class FilterBySponsorListView(LoginRequiredMixin, ListView):
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

class FilterByLiderListView(LoginRequiredMixin, ListView):
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

class LiderListView(LoginRequiredMixin, ListView):
    model = Lider
    template_name = "Projects/master/list_detail_lider.html"
    context_object_name = "LIST_DETAIL_LIDER"

class SponsorListView(LoginRequiredMixin, ListView):
    model = Sponsor
    template_name = "Projects/master/list_detail_sponsor.html"
    context_object_name = "LIST_DETAIL_SPONSOR"

#--------------------------------
#   CREAR todos los registros
#--------------------------------

class TarjetaCreateView(LoginRequiredMixin, CreateView):
    model = Tarjeta
    template_name = "Projects/cards/form_create_cards.html"
    fields = ['lider', 'sponsor', 'titulo', 'descripcion', 'fecha_inicio', 'fecha_fin','estado']
    success_url = reverse_lazy("list_cards")

class LiderCreateView(LoginRequiredMixin, CreateView):
    model = Lider
    template_name = "Projects/master/form_create_lider.html"
    fields = ['nombre']
    success_url = reverse_lazy("list_lider")

class SponsorCreateView(LoginRequiredMixin, CreateView):
    model = Sponsor
    template_name = "Projects/master/form_create_sponsor.html"
    fields = ['nombre']
    success_url = reverse_lazy("list_cards")


#--------------------------------
#   LEER todos los registros
#--------------------------------

class TarjetaDetailView(LoginRequiredMixin, DetailView):
    model = Tarjeta
    template_name = "Projects/cards/detail_cards.html"
    context_object_name = "TARJETAS"

@login_required
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

class TarjetaUpdateView(LoginRequiredMixin, UpdateView):
    model = Tarjeta
    template_name = "Projects/cards/edit_cards.html"
    context_object_name = "TARJETAS"
    fields = ["lider", "sponsor", "titulo", "descripcion", "fecha_inicio", "fecha_fin", "estado"]
    success_url = reverse_lazy("list_cards")

class LiderUpdateView(LoginRequiredMixin, UpdateView):
    model = Lider
    template_name = "Projects/master/edit_lider.html"
    context_object_name = "LIDER"
    fields = ["nombre"]
    success_url = reverse_lazy("list_lider")

class SponsorUpdateView(LoginRequiredMixin, UpdateView):
    model = Sponsor
    template_name = "Projects/master/edit_sponsor.html"
    context_object_name = "SPONSOR"
    fields = ["nombre"]
    success_url = reverse_lazy("list_sponsor")


#--------------------------------
#   BORRAR todos los registros
#--------------------------------

class TarjetaDeleteView(LoginRequiredMixin, DeleteView):
    model = Tarjeta
    template_name = "Projects/cards/form_delete_cards.html"
    context_object_name = "TARJETAS"
    success_url = reverse_lazy("list_cards")

class LiderDeleteView(LoginRequiredMixin, DeleteView):
    model = Lider
    template_name = "Projects/master/form_delete_lider.html"
    context_object_name = "LIDER"
    success_url = reverse_lazy("list_lider")

class SponsorDeleteView(LoginRequiredMixin, DeleteView):
    model = Sponsor
    template_name = "Projects/master/form_delete_sponsor.html"
    context_object_name = "SPONSOR"
    success_url = reverse_lazy("list_sponsor")


# -----------------------------------------------------------------------------
# ----------------------------   PERFILES   -----------------------------------
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


#--------------------------------
#          Crear Usuario
#--------------------------------

def user_creation_view(request):
    if request.method == "GET":
        form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    return render(request, "Projects/profile/form_create_user.html", {"FORM_USER": form})


#--------------------------------
#          Editar Usuario
#--------------------------------
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'Projects/profile/form_edit_user.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user