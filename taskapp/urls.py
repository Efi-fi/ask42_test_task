from django.urls import path
from . import views

app_name = 'taskapp'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('input_page', views.input_page, name='input_page'),
    path('output_page', views.output_page, name='output_page'),
]
