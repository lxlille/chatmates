from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)


urlpatterns = [

    url(r'^$', views.home),
    # Url to login, template in templates/registration/login.html
    url(r'^login/$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/', views.edit_profile, name='edit_profile'),
    url(r'^change-password/', views.change_password, name='change_password'),
    url(r'^profile/(\w*)/$', views.show_profile, name='show_profile'),
    url(r'^reset-password/$', PasswordResetView.as_view(), name='reset_password'),
    url(r'^reset-password/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/', PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    url(r'^reset-password/complete/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]