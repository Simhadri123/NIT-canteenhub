from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the help text for password fields
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None
        self.fields['email'].help_text = None
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class SignInForm(forms.Form):
    username = forms.Field(label='username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

