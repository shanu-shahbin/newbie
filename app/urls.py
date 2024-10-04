from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.conf.urls import handler404


urlpatterns = [
    path('', views.splash, name='splash'),
    path('index/', views.index, name='index'),
    path('search/', views.job_search, name='job_search'),
    path('login/', views.login_view, name='login'),
    path('logout',views.logout,name='logout'),
    path('signup/', views.signup, name='signup'),
    path('company_list',views.company_list,name='company_list'),
    path('company_detail/<int:id>',views.company_detail,name='company_detail'),
    path('job/<int:id>/', views.job_details, name='job_details'),
    path('category/<int:id>/', views.category, name='category'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),





    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),

    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),

    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

]

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
handler404 = custom_404_view

def custom_500_view(request):
    return render(request, '500.html', status=500)
handler500 = custom_500_view