from django.urls import path

from .views import SuccessView, ContactView, AboutProductView



app_name="contactapp"
urlpatterns = [
    path("", ContactView.as_view(), name="contact"),
    path("success/", SuccessView.as_view(), name="success"),
    path("aboutproducts/", AboutProductView.as_view(), name='aboutproduct')
]