from django.shortcuts import render, redirect
from accounts. forms import RegistrationForm, EditProfileFrom
from accounts.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from homepage.views import Friends


def home(request):

    return redirect('/home')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        # Checks if the form is valid
        if form.is_valid():
            form.save()
            return redirect('../../account/login')
    else:
        form = RegistrationForm()
    # Passes the form as an argument to the html template
    args = {'form': form}
    return render(request, 'accounts/reg_form.html', args)


# If the user wants to see and edit hes own profile
def view_profile(request):
    if not request.user.is_authenticated:
        return redirect('../login')
    args = {
        'user': request.user
    }
    return render(request, 'accounts/own_profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileFrom(request.POST, instance=request.user)

        # Checks if the form is valid
        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    else:
        # Checks if user has credentials
        if not request.user.is_authenticated:
            return redirect('../../login')
        else:
            form = EditProfileFrom(instance=request.user)
            # Passes the form as an argument to the html template
    args = {
        'form': form
    }
    return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        # Checks if the form is valid
        if form.is_valid():
            form.save()
            # Lets user to stay logged in
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change-password')

    else:
        # Checks if the user is authenticated
        if not request.user.is_authenticated:
            return redirect('../login')
        else:
            form = PasswordChangeForm(user=request.user)
            # Passes the forms as a argument to the template
            args = {
                'form': form
            }
            return render(request, 'accounts/change_password.html', args)


def show_profile(request, username):
    try:
        user = User.objects.get(username=username)
        args = {
            'user': user
        }
        # Get a friendlist
        flist = Friends(request.user)

        # Deny access for the anonymous user
        if not request.user.is_authenticated:
            return redirect("../../login/")
        # If the user request to see hes own profile
        if user == request.user:
            return redirect('/account/profile', args)
        # if the profile requested is on users friendlist
        if user in flist.acceptedFriends():
            return render(request, "accounts/friends_profile.html", args)
        # If the profile requested is someone else
        else:
            return render(request, 'accounts/user_profile.html', args)

    except User.DoesNotExist:
        return render(request, 'accounts/user_does_not_exist.html')


