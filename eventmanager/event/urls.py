from django.urls import path
from . import views

urlpatterns = [
    # The '' = home page
    path('', views.index, name='index'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('edit/<str:pk>', views.edit, name='edit'),

]