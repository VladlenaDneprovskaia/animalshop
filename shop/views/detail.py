from django.views.generic import DetailView

from shop.models import Product


class DetailProductView(DetailView):
    template_name = 'pages/detail_product.html'
    model = Product
