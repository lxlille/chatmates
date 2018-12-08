from discussion.models import *
import datetime
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse

# Create your views here.

@csrf_protect
def discussion_view(request, number):

    if request.method =='GET':
        # Deny access for the anonymous user
        if not request.user.is_authenticated:
            return redirect("/account/login/")

    # must initialize message for args
    message = " "

    try:
        Discussion.objects.get(discussionNumber=number)
    except Discussion.DoesNotExist:
        # If there is not discussion on wanted number already in database, this creates a new one
        Discussion.objects.create(
            discussionNumber=number,
            createrUser=request.user
        )

    try:
         Discussion.objects.get(discussionNumber=number).users.all()
    except Discussion.DoesNotExist:
        # If there is no users in discussions, creates a one with discussionmember
        DiscussionMember.objects.create(
            discussion=Discussion.objects.get(discussionNumber=number),
            member=request.user
        )

    try:
        Discussion.objects.get(discussionNumber=number).users.all().get(member=request.user)
    except DiscussionMember.DoesNotExist:
        # If user is not yet in discussion, adds user in discussion
        DiscussionMember.objects.create(
            discussion=Discussion.objects.get(discussionNumber=number),
            member=request.user
        )

    args = {
        'userName': str(request.user).capitalize(),
        'chatData': message
    }

    if request.method == 'POST':
        name = request.user

        if 'messageData' in request.POST:
            message = request.POST['messageData']
        else:
            message = "no message in POST"

        # Creates a discussion to database.
        DiscussionMessage.objects.create(
            messageData=message,
            sender=name,
            time=datetime.datetime.now(),
            discussion=Discussion.objects.get(discussionNumber=number)
        )

    return render(request, 'discussion/discussion.html', args)


def getMessageData(request, number):
    json_data = {}
    try:
        # Gets all message from discussion on specific number and makes those a json
        all_messages = Discussion.objects.get(discussionNumber=number).messages.all()
        for message in all_messages:
            json_data[str(message.time)] = str(message.sender) + ": " + message.messageData
    except Discussion.DoesNotExist:
        pass
    return JsonResponse(json_data, content_type="application/json")


def getUsersInDiscussion(request, number):
    json_data = {}
    try:
        # Finds all discussion users
        all_users = Discussion.objects.get(discussionNumber=number).users.all()
        i = 0
        for memberObject in all_users:
            json_data[i] = str(memberObject.member)
            i = i+1
    except Discussion.DoesNotExist:
        pass
    return JsonResponse(json_data, content_type="application/json")

# Finds all messages on discussion number and check if message is send by user who created message
# or user who created discussion and if so then function will delete message from database.
def removeMessage(request, number):
    json_data = {}
    date = request.GET.get('messageData', None)
    discussionCreater = Discussion.objects.get(discussionNumber=number).createrUser
    messages = Discussion.objects.get(discussionNumber=number).messages.all()

    for message in messages:
        if request.user == message.sender or request.user == discussionCreater:
            if str(message.time) == date:
                date = str(message.time)
                message.delete()

    json_data[date] = number
    return JsonResponse(json_data, content_type="application/json")
