from django.urls import path

from .views import AddInCart, PutFromCart, RemoveFromCart, CartView, ClearCart, AddPluraliseInCart

app_name = 'cart'

urlpatterns = [
    path('add/<int:pk>/', AddInCart.as_view(), name='add'),
    path('add-pluralise/<int:pk>/', AddPluraliseInCart.as_view(), name='add-pluralise'),
    path('put/<int:pk>/', PutFromCart.as_view(), name='put'),
    path('remove/<int:pk>', RemoveFromCart.as_view(), name='remove'),
    path('clear/', ClearCart.as_view(), name='clear'),
    path('', CartView.as_view(), name='home')
]
