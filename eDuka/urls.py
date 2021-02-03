from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import path,include
from django.urls import path, include 
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('cart/', views.cart, name='cart'),
    path('checkout/',views.checkout,name ='checkout'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('product/(\d+)', views.product, name='product_results'),   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)