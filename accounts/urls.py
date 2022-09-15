from django.urls import path
from .views import *
from accounts import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('doctor_list',views.doctor_list,name='doctor_list'),
    path('search_doctors',views.search_doctors,name='search_doctors'),
    path('doctor_profile/<int:pk>',views.doctor_profile,name='doctor_profile'),
   # path('doctor_evaluate/<int:pk>',doctor_evaluate.as_view(),name='doctor_evaluate'),
    path('update_profile/<int:pk>',Update_profile.as_view(),name='update_profile'),
    path('update_inform/<int:pk>',Update_profile_inform.as_view(),name='update_inform'),
    path('add_doctor',Add_doctor.as_view(),name='add_doctor'),
    path('comment_page/<int:pk>',commentview.as_view(),name='comment_page'),    
    path('register',Register.as_view(),name='register'),
    path('loginn',views.log,name='loginn'),
    path('password/',auth_views.PasswordChangeView.as_view(
        template_name='change_password.html',
        success_url = reverse_lazy('doctor_list') ),name='password')    
]
