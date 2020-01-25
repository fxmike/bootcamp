from django.urls import path
from . import views

urlpatterns = [
    path('dogs/<int:id>', views.dog, name='dog'),
    path('dogs/', views.dogs),
    path('calc/<eq>/<int:a>/<int:b>', views.calc),
    path('hello/<imie>', views.hello_imie),
    path('texts/<int:ile_gwiazdek>/<user_text>', views.cool_text),
    path('about/', views.about),
    path('', views.index)
]
