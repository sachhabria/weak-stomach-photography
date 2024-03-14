from django.views import generic

# Create your views here.

from .models import Product

class IndexView(generic.ListView):
    template_name = "store/index.html"
    context_object_name = "latest_products"

    def get_queryset(self):
        """Return the last ten published products."""
        return Product.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Product
    template_name = "store/detail.html"
    