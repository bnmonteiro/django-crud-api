from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import PessoaController, PessoaDetailController, PesoIdealController

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('pessoas', PessoaController.as_view(), name='pessoa-list'),
    path('pessoas/<int:pk>', PessoaDetailController.as_view(), name='pessoa-detail'),
    path('pessoas/calculate-peso-ideal', PesoIdealController.as_view(), name='calcular-peso-ideal'),
]
