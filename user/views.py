from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .forms import AuthForm, RegForm, EditForm
from django.contrib.auth import authenticate, login
import django.contrib.auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import View


def print_messages(request, errors):
    for field in errors:
        for error in field.errors:
            messages.error(request, error)


def my_account(request):
    return render(request, 'my-account.html', {'auth_form': AuthForm(), 'reg_form': RegForm()})


class EditAccount(View):
    def get(self, request):
        edit_form = EditForm(initial={'first_name':request.user.first_name,'last_name':request.user.last_name,'email': request.user.email, 'username':request.user.username})
        return render(request, 'edit-account.html', {'edit_form': edit_form})

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        username = user.username
        edit_password_form = EditForm(request.POST)
        if edit_password_form.is_valid():
            edit_password_form = edit_password_form.cleaned_data
            if not (check_password(edit_password_form['old_password'], user.password)):
                messages.error(request, "Неверный пароль")
            else:
                user.set_password(edit_password_form['new_password'])
                user.save()
                messages.info(request, "Пароль успешно изменён")
                user = authenticate(request, username=username, password=edit_password_form['new_password'])
                login(request, user)
        else:
            print_messages(request, edit_password_form)
        return redirect('user:my-account')


def registration(request):
    reg_info = RegForm(request.POST)
    if reg_info.is_valid():
        reg_info = reg_info.cleaned_data
        username = reg_info['email'].split('@')[0]
        user = User.objects.create_user(username, reg_info['email'], reg_info['password'])
        user.save()
        user = authenticate(request, username=username, password=reg_info['password'])
        login(request, user)
    return redirect('user:my-account')


def authorization(request):
    auth_info = AuthForm(request.POST)
    if auth_info.is_valid():
        auth_info = auth_info.cleaned_data
        if (len(User.objects.filter(email=auth_info['login'])) > 0):
            u = User.objects.get(email=auth_info['login'])
        elif (len(User.objects.filter(username=auth_info['login'])) > 0):
            u = User.objects.get(username=auth_info['login'])
        else:
            messages.error(request, 'Такого пользователя нет')
            return redirect('user:my-account')
        user = authenticate(request, username=u.username, password=auth_info['password'])
        login(request, user)
    return redirect('user:my-account')


def logout(request):
    django.contrib.auth.logout(request)
    return redirect('user:my-account')
