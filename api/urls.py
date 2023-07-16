from django.urls import path
from . import views

from django.urls import path
from rest_framework import routers
from api import views
router = routers.SimpleRouter()
router.register(r'api/retete', views.RetetaViewSet)
router.register('api/meniuri', views.MeniuViewSet)
urlpatterns = [
 # path('', views.reteta_list, name='reteta_list'),
]
urlpatterns += router.urls