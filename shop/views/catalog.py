from django.db.models import Q
from django.views.generic import ListView

from shop.forms import FilterForm
from shop.models import Product


class CatalogView(ListView):
    template_name = 'pages/catalog.html'
    model = Product
    paginate_by = 5
    ordering = ('-name',)
    deleted_queries = ['page', 'search']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query_dict = self.request.GET.copy()

        context['filter_form'] = FilterForm(self.request.GET)

        for query_name in self.deleted_queries:
            if query_name in query_dict:
                del query_dict[query_name]

        context['queries'] = query_dict.urlencode()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_form = FilterForm(self.request.GET)

        if 'search' in self.request.GET:
            return queryset.filter(name__icontains=self.request.GET['search'])

        if filter_form.is_valid():
            print(filter_form.__dict__)
            if 'price_range' in filter_form.cleaned_data and filter_form.cleaned_data['price_range'] is not None:
                min_price, max_price = filter_form.cleaned_data['price_range']
                queryset = queryset.filter(price__gte=min_price,
                                           price__lte=max_price)

            if 'weight_range' in filter_form.cleaned_data and filter_form.cleaned_data['weight_range'] is not None:
                min_weight, max_weight = filter_form.cleaned_data['weight_range']
                queryset = queryset.filter(weight__gte=min_weight,
                                           weight__lte=max_weight)

            if 'has_discount' in filter_form.cleaned_data and filter_form.cleaned_data['has_discount']:
                queryset = queryset.exclude(Q(discount=0))

            if 'category' in filter_form.cleaned_data and len(filter_form.cleaned_data['category']) != 0:
                queryset = queryset.filter(animal__in=filter_form.cleaned_data['category'])

            if 'brand' in filter_form.cleaned_data and len(filter_form.cleaned_data['brand']) != 0:
                queryset = queryset.filter(brand__in=filter_form.cleaned_data['brand'])

        return queryset
