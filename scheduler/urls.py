from django.urls import path
from . import views


urlpatterns = [
path('',views.index, name='index'),
path('home/', views.home, name='home'),
path('schedule/', views.schedule_view, name='schedule'),
path('submit/', views.submit_view, name='submit'),
path('success/', views.success_view, name='success'),
path('services/', views.services_view, name='services'),
path('list/', views.list, name='list'),
path('contact/', views.contact_view, name='contact'),
path('user_schedule/', views.user_schedule, name='user_schedule'),
path('schedule/update/<int:pk>/', views.edit_customer, name='edit_customer'),
path('schedule/submit_update/<int:pk>/', views.submit_update_view, name='submit_update'),
path('schedule/delete/<int:pk>/', views.delete_customer, name='delete_customer'),













 
]