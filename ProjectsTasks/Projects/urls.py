from django.urls import path
from .views import(
    home_view,
    TarjetaListView,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("cards-list/", TarjetaListView.as_view(), name="list_cards"),
]
