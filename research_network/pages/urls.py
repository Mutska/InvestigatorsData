from django.urls import path,re_path
from django.conf.urls import url
from . import views
import database.views

#Las urls de toda la aplicacion
urlpatterns = [
    path('', database.views.base, name='base'),
    path('signup/', database.views.user_signup, name='signup'),
    path('activate/<uidb64>/<token>/', database.views.activate, name='activate'),
    path('login/', database.views.user_login, name='login'),
    url(r'logout/$', database.views.user_logout, name='logout'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutOfPageView.as_view(), name='about'),
    path('search/', database.views.user_search, name='search'),
    path('profile/<slug>/', views.UserProfielView.as_view(), name='profile'),
    path('profile/<slug>/edit_profile/', database.views.user_edit, name='edit_profile'),
    path('college/<slug>/', views.college_view, name='college_profile'),
    path('state/<slug>/', database.views.state_search, name='search_profile'),
    path('campus/<slug>/', views.campus_view, name='campus_profile'),
    path('institute/<slug>/', views.institute_view, name='institute_profile'),
    path('subinstitute/<slug>/', views.subinstitute_view, name='subinstitute_profile'),
    path('paper/<slug>/', views.paper_view, name='paper_profile'),
    path('group/<slug>/', views.group_view, name='group_profile'),
    path('reset/',database.views.email_reset, name='change_password_sent'),
    path('reset/<uidb64>/<token>/',database.views.reset_password, name='changePassword'),
    path('profile/<slug>/groups/', database.views.group_list, name="group_list"),
    path('help-home/', views.HomeHelp.as_view(), name = 'help_home'),
    path('help-register/', views.RegisterHelp.as_view(), name = 'help_register'),
    path('help-login/', views.LoginHelp.as_view(), name = 'help_login'),


]
