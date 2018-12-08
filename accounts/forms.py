from django import forms
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget = forms.TextInput(attrs={'class' : 'form-control'}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  'bio',
                  'birth_date',
                  'location',
                  'workplace',
                  )
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'birth_date': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'workplace': forms.TextInput(attrs={'class': 'form-control'}),

        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.firs_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.bio = self.cleaned_data['bio']
        user.birth_date = self.cleaned_data['birth_date']
        user.location = self.cleaned_data['location']
        user.workplace = self.cleaned_data['workplace']

        if commit:
            user.save()

        return user


class EditProfileFrom(UserChangeForm):

    class Meta:
        model = User
        fields = (
                  'first_name',
                  'last_name',
                  'bio',
                  'birth_date',
                  'location',
                  'workplace',
                  'password',
                  )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'workplace': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),

        }
