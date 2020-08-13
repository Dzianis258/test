from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, ProfileImageForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required #декоратор


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан.')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/registration.html',
                  {
                      'title':'Страница регистрации',
                      'form': form,
                  }
                  )


@login_required
def profile(request):
    if request.method == 'POST':
        profileForm = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        updateForm = UserUpdateForm(request.POST, instance=request.user)
        if profileForm.is_valid() and updateForm.is_valid():
            updateForm.save()
            profileForm.save()
            messages.success(request, 'Ваш аккаунт был успешно обнавлен.')
            return redirect('profile')
    else:
        profileForm = ProfileImageForm(instance=request.user.profile)
        updateForm = UserUpdateForm(instance=request.user)
    date = {
        'profileForm': profileForm,
        'updateForm': updateForm
    }

    return render(request, 'users/profile.html', context=date)