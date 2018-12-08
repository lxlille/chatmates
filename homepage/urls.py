from django.conf.urls import url
from homepage.views import Homepage
from homepage.views import acceptFriend, declineFriend, cancelFriend, rmFriend


urlpatterns = [
    # The only url for the homepage
    url(r'^$', Homepage.as_view(), name='home'),
    url(r'ajax/acceptFriend/', acceptFriend, name='acceptFriend'),
    url(r'ajax/declineFriend/', declineFriend, name='declineFriend'),
    url(r'ajax/cancelFriend/', cancelFriend, name='cancelFriend'),
    url(r'ajax/rmFriend/', rmFriend, name='rmFriend')

]