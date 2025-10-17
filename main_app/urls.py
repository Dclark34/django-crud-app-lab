from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.about, name="about"),
    path('parks/', views.park_index, name='park-index'),
    path('parks/<int:park_id>/', views.park_detail, name='park-detail'),
    path('parks/create/', views.ParkCreate.as_view(), name='park-create'),
    path('parks/<int:pk>/update/', views.ParkUpdate.as_view(), name='park-update'),
    path('parks/<int:pk>/delete/', views.ParkDelete.as_view(), name='park-delete'),
    path('parks/<int:park_id>/add-log/', views.add_log, name='add-log'),
    path('accounts/signup/', views.signup, name='signup'),
    path('log/<int:pk>/update/', views.LogUpdate.as_view(), name='log-update'),
    path('log/<int:pk>/delete/', views.LogDelete.as_view(), name='log-delete'),
]