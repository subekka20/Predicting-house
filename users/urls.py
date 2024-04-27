from django.urls import path
from .views import login, signup, admin_dashboard, home, houses, new_house, booking, profile
from . import views
# app_name = 'users'
urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('<int:user_id>/home/', home, name='home'),
    path('houses/', houses, name='houses'),
    path('new_house/', new_house, name='new_house'),
    path('booking/<int:house_id>/', booking, name='booking'),
    path('<int:user_id>/profile/', profile, name='profile'),
    path('<int:user_id>/filtered_page/', views.filtered_page, name='filtered_page'),
    # path('reply_booking/<int:booking_id>/', views.reply_booking, name='reply_booking'),
    # path('mark_as_sold/<int:booking_id>/', views.mark_as_sold, name='mark_as_sold'),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    # path('delete_booking/<int:booking_id>/', views.delete_booking_admin, name='delete_booking_admin'),

]