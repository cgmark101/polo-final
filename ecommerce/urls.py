from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("acerca", views.acerca, name="acerca"),
    path("contacto", views.contacto, name="contacto"),
    path('products/', views.all_products, name='products'),
    path('category/', views.category, name='categoria'),
    path('producto/<int:producto_id>/', views.detail_products, name="producto"),
    path('categorias/all/', views.category, name="categorias"),
    path('categoria/<str:cat>/', views.detail_category, name="categoria"),
    path('busqueda', views.search, name="search")
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)