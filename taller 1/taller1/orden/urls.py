from django.urls import path
from .views import *

urlpatterns = [
    path("", homePageView.as_view(), name= "home"),
    path("/crear", crear.as_view() , name="crear"),
    path("/visualizacion", ver.as_view() , name="ver"),
    path('products/<str:id>', mostrar.as_view(), name='mostrar'),
    path("exito", exito.as_view() , name="exito"),
    path('borrar/<str:id>/', borrar.as_view(), name='borrar'),

]