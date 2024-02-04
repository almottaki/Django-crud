from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.add_todo, name="create_todo"),
    path("<int:id>/update/", views.update_todo, name="update_todo"),
    path("<int:id>/delete/", views.delete_todo, name="delete_todo"),
    path("<int:id>/details/", views.details_todo, name="details_todo"),
]
