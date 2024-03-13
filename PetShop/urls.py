from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from PetShop.view import HomeView

urlpatterns = ([
                   path('admin/', admin.site.urls),
                   path('shop/', include('shop.urls', namespace='shop')),
                   path('auth/', include('appauth.urls', namespace='appauth')),
                   path('cart/', include('cart.urls', namespace='cart')),
                   path('', HomeView.as_view(), name='home'),
               ]
               + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
