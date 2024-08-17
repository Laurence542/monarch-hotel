from django.conf.urls.static import static
from django.conf import settings
from . import views
from.views import about, check_out
from.views import feature
from.views import sign_up
from.views import admin_dashboard
from.views import rooms_display
from.views import hotel_section1
from.views import add_hotel
from.views import base_dashboard
from.views import base_sidebarr
from.views import card_payment
from.views import payment_option
from.views import success_message
from.views import admins_success
from.views import user_views
from.views import view_users
from .views import resturant_dining
from .views import catering_conference
from .views import delete_hotel
from .views import delete_information
from.views import delete_signup
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/',about, name = "about"),
    path('delete_signup/<int:signup_id>/', delete_signup, name='delete_signup'),
    path('feature/',feature, name = "feature"),
    path('delete_information/<int:information_id>/', delete_information, name='delete_information'),
    path('resturant_dinings/',resturant_dining, name = "resturant_dinings"),
    path('admin1/', admin_dashboard, name='admin1'),
    path('catering_conference/', catering_conference, name='catering_conference'),
    path('room/', rooms_display, name='room'),
    path('hotel/delete/<int:hotel_id>/', delete_hotel, name='delete_hotel'),
    path('success/', success_message, name='success'),
    path('check/', check_out, name='check'),
    path('card/', card_payment, name='card'),
    path('adminn_sucess/', admins_success, name='adminn_sucess'),
    path('userview/', view_users, name='userview'),
    path('create/', add_hotel, name='create'),
    path('payment_option/', payment_option, name='payment_option'),
    path('baseadmin/', base_dashboard, name='baseadmin'),
    path('sideadmin/', base_sidebarr, name='sideadmin'),
    path('signup/', sign_up, name='signup'),
    path('hotel1/', hotel_section1, name='hotel1'),
    path('userviews/', user_views, name='userviews'),
    path('login/', views.login_page, name='login'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
