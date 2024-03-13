from django.urls import path

from .views import CatalogView, DetailProductView

app_name = 'shop'
urlpatterns = [
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('detail/<int:pk>', DetailProductView.as_view(), name='detail'),
]
