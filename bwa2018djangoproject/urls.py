"""bwa2018djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from bwa2018djangoproject import views as bwa_views

urlpatterns = [
    url(r'^$', bwa_views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    url(r'^home/', include('homepage.urls')),
    url(r'^discussion/', include(('discussion.urls', 'discussion'), namespace='discussion')),
    # Added this url for the email reset passwords to work in the accounts-app
    url(r'', include('django.contrib.auth.urls')),
    # Redirects user from the reset-password page to the correct login page
    url(r'account/login/', bwa_views.login_redirect, name='login_redirect'),

]

