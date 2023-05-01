from django.urls import path

from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('contacts/', contact),
    path('new/', new),
]
