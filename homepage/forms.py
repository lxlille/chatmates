from django import forms
from homepage.models import Friendship


class addFriendForm(forms.Form):

    receiver = forms.CharField(label='Username', widget = forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = Friendship
        fields = ('receiver',)

