from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.db.models import Q
from accounts.models import User
from django.http import JsonResponse
import datetime

from .models import Friendship
from discussion.models import DiscussionMember
from .forms import addFriendForm
# Create your views here.


class Friends:
    # Class to get the friends from the models

    def __init__(self, username):
        self.user = username

    def acceptedFriends(self):
        data = Friendship.objects.all().filter(Q(sender=self.user) |
                                               Q(receiver=self.user)).filter(status='accepted')
        friendlist = []
        for obj in data:
            if obj.receiver == self.user:
                friendlist.append(obj.sender)
            elif obj.sender == self.user:
                friendlist.append(obj.receiver)
        return friendlist

    def sendRequests(self):
        data = Friendship.objects.all().filter(sender=self.user).filter(status='pending')
        requestlist = []
        for obj in data:
            package = {
                'receiver': obj.receiver,
                'time': obj.sendTime
            }
            requestlist.append(package)

        return requestlist

    def receivedRequest(self):
        data = Friendship.objects.all().filter(receiver=self.user).filter(status='pending')
        requestlist = []
        for obj in data:
            package = {
                'sender': obj.sender,
                'time': obj.sendTime
            }
            requestlist.append(package)

        return requestlist


def rmFriend(request):
    user = request.user
    friendName = request.GET.get('friend', None)
    data = {
        'done': False,
        'friend': friendName
    }

    try:
        friend = User.objects.get(username=friendName)
        if friend:
            try:
                ship = Friendship.objects.get(sender=user, receiver=friend)
                if ship:
                    if ship.status == "accepted":
                        ship.delete()
                        data['done'] = True
            except Friendship.DoesNotExist:
                try:
                    ship = Friendship.objects.get(sender=friend, receiver=user)
                    if ship:
                        if ship.status == "accepted":
                            ship.delete()
                            data['done'] = True
                except Friendship.DoesNotExist:
                    pass
    except User.DoesNotExist:
        pass

    return JsonResponse(data)


def acceptFriend(request):
    user = request.user
    friendName = request.GET.get('friend', None)
    data = {
        'done': False,
        'friend': friendName
    }

    try:
        friend = User.objects.get(username=friendName)
        if friend:
            try:
                ship = Friendship.objects.get(sender=friend, receiver=user)
                if ship:
                    if ship.status == "pending":
                        ship.status = "accepted"
                        ship.save()
                        data['done'] = True
            except Friendship.DoesNotExist:
                pass
    except User.DoesNotExist:
        pass

    return JsonResponse(data)


def declineFriend(request):
    user = request.user
    friendName = request.GET.get('friend', None)
    data = {
        'done': False,
        'friend': friendName
    }

    try:
        friend = User.objects.get(username=friendName)
        if friend:
            try:
                ship = Friendship.objects.get(sender=friend, receiver=user)
                if ship:
                    if ship.status == "pending":
                        ship.delete()
                        data['done'] = True
            except Friendship.DoesNotExist:
                pass
    except User.DoesNotExist:
        pass

    return JsonResponse(data)


def cancelFriend(request):
    user = request.user
    friendName = request.GET.get('friend', None)
    data = {
        'done': False,
        'friend': friendName
    }

    try:
        friend = User.objects.get(username=friendName)
        if friend:
            try:
                ship = Friendship.objects.get(sender=user, receiver=friend)
                if ship:
                    if ship.status == "pending":
                        ship.delete()
                        data['done'] = True
            except Friendship.DoesNotExist:
                pass
    except User.DoesNotExist:
        pass

    return JsonResponse(data)


class Homepage (TemplateView):
    template_name = 'homepage/homepage.html'

    def getArgs(self, request):
        # Function to get the arguments for the return
        # Name to greet the user
        name = str(request.user).capitalize()
        # Form to add a friend
        form = addFriendForm()
        # Data of friends and requests
        friendData = Friends(request.user)

        discussions = {}

        try:
            discussions = DiscussionMember.objects.filter(member=request.user)
        except:
            pass

        args = {
            'myName': name,
            'user': request.user,
            'discussions' : discussions,
            'friends': friendData.acceptedFriends(),
            'requestSend': friendData.sendRequests(),
            'requestReceived': friendData.receivedRequest(),
            'form': form,
        }

        return args


    def get(self, request):

        # Deny access for the anonymous user
        if not request.user.is_authenticated:
            return redirect("../account/login/")

        args = self.getArgs(request)

        return render(request, self.template_name, args)


    def post(self, request):

        # Deny access for the anonymous user
        if not request.user.is_authenticated:
            return redirect("../account/login/")

        # Check which form is submitted
        if 'addFriend' in request.POST:

            # Arguments to pass on to the template if something goes wrong
            args = self.getArgs(request)

            # Form to add a friend
            form = addFriendForm(request.POST)

            if form.is_valid():
                username = form['receiver'].value()
                friendUser = None

                try:
                    friendUser = User.objects.get(username=username)
                except User.DoesNotExist:
                    pass

                if friendUser:
                    # Check if the the user is already a friend or a request is pending
                    friendData = Friends(request.user)
                    senders = []
                    receivers = []
                    text = ""

                    for request1 in friendData.sendRequests():
                        receivers.append(request1.get('receiver'))
                    for request2 in friendData.receivedRequest():
                        senders.append(request2.get('sender'))

                    if friendUser.username == request.user.username:
                        text = "That's your username, you silly"

                    elif friendUser in friendData.acceptedFriends():
                        text = "User is already your friend"

                    elif friendUser in receivers:
                        text = "You have already sent a friend request to this person"

                    elif friendUser in senders:
                        text = "Check your notifications, you're in for a surprise"

                    else :
                        # All ok, send the request
                        friend = Friendship.objects.create(
                            receiver=friendUser,
                            sender = request.user,
                            sendTime = datetime.datetime.now(),
                            status = "pending"
                        )
                        friend.save()
                        text = "Congrats, the friend request is on its way"
                else:
                    text = "User not found, check for typos"

                # Arguments to pass on to the template if things go well
                args = self.getArgs(request)

                # Pass the modified form
                args['form'] = form
                args['text'] = text

            return render(request, self.template_name, args)

