from django.shortcuts import get_object_or_404, render
from .models import ProductInfo
from django.views import generic
from django.urls import reverse


# Create your views here.


class IndexView(generic.ListView):
    template_name = "products/index.html"
    context_object_name = "products_list"

    def get_queryset(self):
        """Return all the objects, in this case all the products."""
        return ProductInfo.objects.all().order_by('-pk')
    

class DetailView(generic.DetailView):
    model = ProductInfo
    template_name = "products/detail.html"

def about(request):
    return render(request, "products/about.html", {}) #products/about its the path on the file, not the url

def contact(request):
    return render(request, "products/contact.html", {})

