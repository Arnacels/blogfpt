from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from blog.models import Post


# Create your views here.
@login_required(redirect_field_name='/accounts/login/')
def cabinet(request):
    user = request.user
    post = Post.objects.filter(creator=user)
    return render(request, 'user/profile.html', {'user': user, 'posts': post})


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'user/registration.html', {'form': form})


@login_required(redirect_field_name='/accounts/login/')
def logout_user(request):
    logout(request)
    return redirect('/')
