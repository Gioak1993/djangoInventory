from django.urls import path

from . import views

app_name = "products"
urlpatterns = [
    # ex: /products/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /products/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]
