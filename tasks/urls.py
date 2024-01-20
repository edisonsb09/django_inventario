from django.urls import path
from .views import home, menu, login_view, producto,proveedor,pedidos, cliente

urlpatterns = [
    path('', home, name='home'),
    # path('inicio/', views.inicio, name='inicio'),  
    # path('login/', views.views, name='login'),  
    path('menu/', menu, name='menu'),  
    path('login/', login_view, name='login'),
    path('producto/', producto, name='producto'),
    path('pedidos/', pedidos, name='pedidos'),
    path('cliente/', cliente, name='cliente'),
    path('proveedor/', proveedor, name='proveedor'),

]
