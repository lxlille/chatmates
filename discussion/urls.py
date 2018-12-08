from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^([0-9]*)/$', views.discussion_view, name="discussionPage"),
    url(r'ajax/discussionData/([0-9]*)/', views.getMessageData),
    url(r'ajax/discussionMembers/([0-9]*)/', views.getUsersInDiscussion),
    url(r'ajax/discussionDataMessageRemove/([0-9]*)/', views.removeMessage)
]
