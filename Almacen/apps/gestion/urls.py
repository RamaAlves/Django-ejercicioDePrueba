from django.urls import path

from . import views

app_name = "gestion"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.show, name="show"),
    path('create', views.create, name="create"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
]
