from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_us, name='about_us'),
    path('rating-options/', views.rating_options, name='rating_options'),
    path('contact/', views.contact_us, name='contact_us'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('company/<str:company_name>/', views.company_profile, name='company_profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('seeker-dashboard/', views.seeker_dashboard, name='seeker_dashboard'),
    path('employer-dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('apply/<int:pk>/', views.apply_job, name='apply_job'),
    path('profile/<str:username>/', views.seeker_profile, name='seeker_profile'),
    path('notifications/', views.notifications, name='notifications'),
    path('candidates/', views.candidates_list, name='candidates_list'),
    path('add-review/', views.add_review, name='add_review'),
    path('add-candidate-rating/', views.add_candidate_rating, name='add_candidate_rating'),
   
]
