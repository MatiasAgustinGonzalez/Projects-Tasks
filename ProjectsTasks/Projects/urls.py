from django.urls import path
from .views import(
    home_view,
    TarjetaListView,
    FilterBySponsorListView,
    FilterByLiderListView,
    LiderListView,
    SponsorListView,
    TarjetaCreateView,
    LiderCreateView,
    SponsorCreateView,
    TarjetaDetailView,
    TarjetaUpdateView,
    LiderUpdateView,
    SponsorUpdateView,
    tarjeta_search_view,
    TarjetaDeleteView,
    LiderDeleteView,
    SponsorDeleteView,
    user_creation_view,
    UserUpdateView,
    user_login_view,
    user_logout_view,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("cards-list/", TarjetaListView.as_view(), name="list_cards"),
    path("cards-filter-bysponsor/<str:sponsor_name>/", FilterBySponsorListView.as_view(), name="filter_sponsor"),
    path("cards-filter-bylider/<str:lider_name>/", FilterByLiderListView.as_view(), name="filter_lider"),
    path("lider-list/", LiderListView.as_view(), name="list_lider"),
    path("sponsor-list/", SponsorListView.as_view(), name="list_sponsor"),
    path("cards-create/", TarjetaCreateView.as_view(), name="create_cards"),
    path("lider-create/", LiderCreateView.as_view(), name="create_lider"),
    path("sponsor-create/",SponsorCreateView.as_view(), name="create_sponsor"),
    path("cards-detail/<int:pk>/", TarjetaDetailView.as_view(), name="detail_cards"),
    path("cards/<int:pk>/update/", TarjetaUpdateView.as_view(), name="update_cards"),
    path("lider/<int:pk>/update/", LiderUpdateView.as_view(), name="update_lider"),
    path("sponsor/<int:pk>/update/", SponsorUpdateView.as_view(), name="update_sponsor"),
    path("cards/search/", tarjeta_search_view, name="search_cards"),
    path("cards-delete/<int:pk>/", TarjetaDeleteView.as_view(), name="delete_cards"),
    path("lider-delete/<int:pk>/", LiderDeleteView.as_view(), name="delete_lider"),
    path("sponsor-delete/<int:pk>/", SponsorDeleteView.as_view(), name="delete_sponsor"),
    path("user-create/", user_creation_view, name="create_user"),
    path('user-edit/', UserUpdateView.as_view(), name='edit_user'),
    path("login/", user_login_view, name="login"),
    path("logout/", user_logout_view, name="logout"),
]
