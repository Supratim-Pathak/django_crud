from django.urls import path
from .views import *
from mycrudApp import views
urlpatterns = [
    path('', views.indexPage),
    path('deleteData/<int:id>', views.deleteData , name='deleteData'),
    path('updateData/<int:id>', views.updateData , name='updateData'),
]      