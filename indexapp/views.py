from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect



from indexapp.forms import LoginForm
from taskapp.models import User


def index_view(request):
    form = LoginForm()
    valuenext = request.POST.get('next')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data.get('username_or_email')
            raw_password = form.cleaned_data.get('password')
            is_email=False
            found=False
            for i in username_or_email:
                if i =="@":
                    is_email=True
            if is_email:
                if not User.objects.filter(email=username_or_email).exists():
                    username_not_found = True
                else:
                    found = True
                    username=User.objects.get(email=username_or_email).username

            if not is_email:
                if not User.objects.filter(username=username_or_email).exists():
                    username_not_found = True
                else:
                    found=True
                    username = User.objects.get(username=username_or_email).username
            if found:
                user = authenticate(username=username, password=raw_password)
                if user is not None:
                    login(request, user)
                    # if request.user.is_superuser:
                    #     return redirect('/admin')
                    # elif request.user.is_employee:
                    return redirect('/dashboard/')
                else:
                    password_error = True
        else:
            form = LoginForm(request.POST)
    return render(request,"indexapp/index.html",locals())

@login_required(login_url="/")
def logout_view(request):
    logout(request)
    return  redirect("/")
