from django.urls import path

from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add/', views.AddView.as_view(), name='add'),
    path('<int:pk>/remove/', views.RemoveView.as_view(), name='delete'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
]
