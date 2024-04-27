from django.urls import path
from .views import(
    home_view,
    TarjetaListView,
    FilterBySponsorListView,
    FilterByLiderListView,
    TarjetaCreateView,
    LiderCreateView,
    SponsorCreateView,
    TarjetaDetailView,
    TarjetaDeleteView,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("cards-list/", TarjetaListView.as_view(), name="list_cards"),
    path("cards-filter-bysponsor/<str:sponsor_name>/", FilterBySponsorListView.as_view(), name="filter_sponsor"),
    path("cards-filter-bylider/<str:lider_name>/", FilterByLiderListView.as_view(), name="filter_lider"),
    path("cards-create/", TarjetaCreateView.as_view(), name="create_cards"),
    path("lider-create/", LiderCreateView.as_view(), name="create_lider"),
    path("sponsor-create/",SponsorCreateView.as_view(), name="create_sponsor"),
    path("cards-detail/<int:pk>/", TarjetaDetailView.as_view(), name="detail_cards"),
    path("cards-delete/<int:pk>/", TarjetaDeleteView.as_view(), name="delete_cards"),
]
