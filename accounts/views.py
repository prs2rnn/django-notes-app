from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpRequest
from django.shortcuts import redirect, render

from .forms import LoginForm, ProfileForm, RegisterForm, UserUpdateForm
from .models import Profile


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

    return render(request, 'accounts/register.html', {'form': form})


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, f'Welcome back, {form.get_user().username}')
        return super().form_valid(form)


@login_required
def profile(request: HttpRequest):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            avatar_deleted = request.POST.get('avatar-deleted') == '1'
            profile = profile_form.save(commit=False)

            if avatar_deleted and profile.avatar:
                profile.avatar.delete(save=False)
                profile.avatar = None

            has_changed = (
                user_form.has_changed() or profile_form.has_changed() or avatar_deleted
            )

            if has_changed:
                user_form.save()
                profile.save()
                messages.success(request, 'Profile updated')
            else:
                messages.info(request, 'No changes were made')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    notes_count = request.user.notes.count()

    return render(
        request,
        'accounts/profile.html',
        {
            'user_form': user_form,
            'profile_form': profile_form,
            'notes_count': notes_count,
        },
    )
