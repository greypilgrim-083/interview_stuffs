from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('signup/', views.signup_view, name='signup'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('logout/', views.logout_view, name='logout'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/vote/<str:vote_type>/', views.vote_post, name='vote_post'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
]
