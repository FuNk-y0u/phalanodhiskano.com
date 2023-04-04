from django.urls import path
from . import views

urlpatterns = [
        path("",views.index, name="index"),
        path("id/<int:id>", views.id, name="id"),
        path("id/", views.id_def, name="id_def"),
]
