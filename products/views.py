from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from .models import ProductInfo
from django.views import generic
from django.urls import reverse
from django.db.models import Q


# Create your views here.


class IndexView(generic.ListView):
    template_name = "products/index.html"
    context_object_name = "products_list"
    paginate_by = 15

    def get_queryset(self):
        """Return the objects that are set as show_onstore = TRUE on the database"""
        return ProductInfo.objects.filter(show_onstore=True).order_by('-pk')
        
    
#view for the home
    
class HomeView(generic.ListView):
    template_name = "products/home.html"
    context_object_name = "latest_products"

    def get_queryset(self):
        """Return all the objects that are set as show_onstore = TRUE on the database"""
        return ProductInfo.objects.filter(show_onstore=True).order_by('-pk')[:5]

class DetailView(generic.DetailView):
    model = ProductInfo
    template_name = "products/detail.html"

def about(request):
    return render(request, "products/about.html", {}) #products/about its the path on the file, not the url

def contact(request):
    return render(request, "products/contact.html", {})

def home(request):
    return render(request, "products/home.html", {})


class SearchResultsView(generic.ListView):
    model = ProductInfo
    template_name = "products/search.html"

    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get("q")
        object_list = ProductInfo.objects.filter(Q(title_text__icontains= query) | Q(category__name_text__icontains = query))

        return object_list
    

