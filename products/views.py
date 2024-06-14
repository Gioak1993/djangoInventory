from typing import Any
from django.db.models.query import QuerySet
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from .models import ProductInfo
from django.views import generic
from django.urls import reverse
from django.db.models import Q
from contactapp.forms import AboutProduct
from django.core.mail import send_mail
from django.conf import settings



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
    context_object_name = 'productinfo'
     

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AboutProduct()
        return context
    
    def post(self, request, *args, **kwargs):
        form = AboutProduct(request.POST)
        product = self.get_object()
        if form.is_valid():
            # Process the form data
            email = form.cleaned_data.get("email")
            subject = form.cleaned_data.get("subject")
            message = form.cleaned_data.get("message")
            
            full_message = f"""
            Received message below from {email}, {subject}, 
            Regarding your product: {product.title_text}
            ________________________


            {message}
            """
            # Send email
            send_mail(
                subject="Received contact form submission",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=settings.NOTIFY_EMAIL,
            )
            # Redirect or signal in some way that the message was sent
            return redirect('contactapp:success')  # Change to an appropriate URL

        # If form is not valid, return to the same detail page with errors
        self.object = self.get_object()
        context = self.get_context_data(object=self.object, contact_form=form)
        return self.render_to_response(context)


def about(request):
    return render(request, "products/about.html", {}) #products/about its the path on the file, not the url

def contact(request):
    return render(request, "products/contact.html", {})

def home(request):
    return render(request, "products/home.html", {})


class SearchResultsView(generic.ListView):
    model = ProductInfo
    template_name = "products/search.html"
    paginate_by = 15

    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get("q")
        object_list = ProductInfo.objects.filter(Q(title_text__icontains = query) | Q(category__name_text__icontains = query))
        object_list_show = object_list.filter(show_onstore=True)
        return object_list_show
    

