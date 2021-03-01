from django.urls import path
from mainpage import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('notice/', views.NoticeListView.as_view(), name='notice'),
    path('notice/<int:pk>', views.NoticeDetailView.as_view(), name='notice-detail'),
]