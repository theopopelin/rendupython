from django.urls import path
from . import views
app_name = 'legends'
urlpatterns = [
    path('', views.index, name='index'), 
    path('add/', views.add, name='add'),
    path('edit/<int:legend_id>/', views.edit, name='edit'),
    path('delete/<int:legend_id>/', views.delete, name='delete'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:legend_id>/', views.update, name='update'),
]