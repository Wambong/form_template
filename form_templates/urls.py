
from django.urls import path
from .views import get_form, form_input

urlpatterns = [
    path('get_form/', get_form, name='get_form'),
    path('', form_input, name='form_input'),
]
