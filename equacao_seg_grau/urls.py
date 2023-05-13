from django.urls import path

from . import views

urlpatterns = [
    path("", views.eq_seg_grau, name="eqwuacao_seg_grau"),
]