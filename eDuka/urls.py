from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from django.conf.urls import path,include
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include 
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('cart/', views.cart, name='cart'),
    path('checkout/',views.checkout,name ='checkout'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    
    
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)