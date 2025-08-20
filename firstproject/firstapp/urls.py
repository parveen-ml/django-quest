from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('function', views.hello_world),
    path('class', views.HelloEthiopia.as_view()),
]