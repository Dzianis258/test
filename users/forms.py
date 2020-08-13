from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


gender_choices = [
    ('мужской', 'Мужской пол'),
    ('женский', 'Женский пол')
]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Введите email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'})
    )
    username = forms.CharField(
        label='Введите имя',
        required=True,
        help_text='Нельзя вводить символы @, /',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'})
    )
    # some = forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control',  'placeholder': 'Введите пароль'})
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Подтвердите пароль'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Введите email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'})
    )
    username = forms.CharField(
        label='Введите имя',
        required=True,
        help_text='Нельзя вводить символы @, /',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(required=False, label='Загрузить фото:', widget = forms.FileInput)

    gender = forms.ChoiceField(
        label='Выберите пол*',
        widget = forms.Select(attrs={'class': 'custom-select'}),
        choices=gender_choices
    )

    get_notifications = forms.BooleanField(
        label='',
        required=False,
        help_text='Соглашение про отправку уведомлений на почту',
    )

    class Meta:
        model = Profile
        fields = ['img', 'gender', 'get_notifications']
