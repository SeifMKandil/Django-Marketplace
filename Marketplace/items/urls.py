from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('', views.search, name='search'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete', views.deleteitem, name='delete'),
    path('<int:pk>/edit', views.editItem, name='edit'),
    path('new/', views.newItem, name='new'),
    
]