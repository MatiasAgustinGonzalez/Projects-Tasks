from django.urls import path
from .views import(
    home_view,
    TarjetaListView,
    TarjetaCreateView,
    FilterBySponsorListView,
    FilterByLiderListView,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("cards-list/", TarjetaListView.as_view(), name="list_cards"),
    path("cards-create/", TarjetaCreateView.as_view(), name="create_cards"),
    path("cards-filter-bysponsor/<str:sponsor_name>/", FilterBySponsorListView.as_view(), name="filter_sponsor"),
    path("cards-filter-bylider/<str:lider_name>/", FilterByLiderListView.as_view(), name="filter_lider"),
]
