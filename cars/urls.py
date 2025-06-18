from django.urls import path
from django.conf.urls.static import static
from cars import views

app_name = 'cars'

urlpatterns = [
    path('', views.cars_view, name='cars_view'),
] 