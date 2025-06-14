from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls',namespace='cart')),  # ← OK if 'products' is your app
    path('orders/', include('orders.urls',namespace='orders')),  # ← OK if 'products' is your app
    path('', include('products.urls' , namespace='products')),  # ← OK if 'products' is your app
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

