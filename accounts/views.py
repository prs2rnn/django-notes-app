from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpRequest
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm


def register(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('notes_list')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, 'Account created')

            return redirect('notes_list')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, f'Welcome back, {form.get_user().username}')
        return super().form_valid(form)
