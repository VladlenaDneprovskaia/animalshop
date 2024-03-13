from django.views.generic import TemplateView

from shop.models import Animal, Product


class HomeView(TemplateView):
    template_name = 'home.html'
    extra_context = {
        'animals': Animal.objects.all(),
        'dog_best': Animal.objects.filter(title='Собака').first().get_products().order_by('-discount').first(),
        'cat_best': Animal.objects.filter(title='Кот').first().get_products().order_by('-discount').first(),
        'best_product': Product.objects.all().order_by('-discount').first(),
        'products': Product.objects.all()
    }
