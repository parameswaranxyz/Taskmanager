from django.urls import path

from Task_manager import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('edit',views.edit,name='edit')
]
