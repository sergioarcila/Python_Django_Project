from django.urls import path, include
from . import views


urlpatterns = [
    path('example/', views.example, name='example'),
    path('view/<uuid>', views.view_profile, name='view_profile'),
    path('all/', views.all_profiles, name='all_profiles'),
    path('edit/<uuid>/', views.edit_profile, name='edit_profile'),
    path('signup/', views.new_user, name='sign_up'),
    path('create/', views.new_profile, name='create'),
    path('home/', views.home_profile, name='profile_home')
]
