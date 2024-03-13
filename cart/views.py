from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from cart.service import Cart


# from shop.models import Product


class AddInCart(View):
    def post(self, *args, **kwargs):
        pk = kwargs['pk']
        cart = Cart(self.request)
        cart.add(pk)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class AddPluraliseInCart(View):
    def post(self, *args, **kwargs):
        pk = kwargs['pk']
        cart = Cart(self.request)
        count = self.request.POST.get('count', 1)
        cart.add_pluralise(pk, int(count))

        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class PutFromCart(View):
    def post(self, *args, **kwargs):
        pk = kwargs['pk']
        cart = Cart(self.request)
        cart.put(pk)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class RemoveFromCart(View):
    def post(self, *args, **kwargs):
        pk = kwargs['pk']
        cart = Cart(self.request)
        cart.remove(pk)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class ClearCart(View):
    def post(self, *args, **kwargs):
        cart = Cart(self.request)
        cart.clear()
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class CartView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/cart.html'
    login_url = reverse_lazy('appauth:login')

