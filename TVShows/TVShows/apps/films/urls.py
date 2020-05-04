from django.urls import path
from . import views

app_name = 'films'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:film_id>/', views.detail, name='detail'),

]