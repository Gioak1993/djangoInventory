from django.urls import path

from . import views

app_name = "products"
urlpatterns = [
    # ex: /products/
    path("products/", views.IndexView.as_view(), name="index"),
    # ex: /products/5/
    path("products/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("about/", views.about, name="about" ),
    path("contact/", views.contact, name="contact"),
    path("", views.HomeView.as_view(), name="home"),
    path("products/search", views.SearchResultsView.as_view(), name="search"),

]
