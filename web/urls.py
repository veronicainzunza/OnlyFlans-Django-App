from django.urls import path, include
from .views import index, about, welcome, contacto, registro_exitoso, map_view, detalle_flan, FlanCreateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('welcome/', welcome, name='welcome'),
    path('contacto/', contacto, name='contacto'),
    path('contacto_exito/', registro_exitoso, name='registro_exitoso'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', include('django.contrib.auth.urls')),
    #path('logout/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('map/', map_view, name='mapa'),
    path('flan/<int:flan_id>/', detalle_flan, name='detalle_flan'),  
    path("crear/", FlanCreateView.as_view(), name='crear'),
]












