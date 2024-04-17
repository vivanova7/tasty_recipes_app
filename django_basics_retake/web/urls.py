from django.urls import path

from django_basics_retake.web.views import index

urlpatterns = (
    path('', index, name='index'),

)