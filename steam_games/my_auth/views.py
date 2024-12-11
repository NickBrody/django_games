from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.generic import FormView
from .forms import CustomLoginForm, CustomUserCreationForm
from .models import Profile
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'my_auth/register.html'
    success_url = reverse_lazy("add_note_on_site:add_note")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response
    
    def form_invalid(self, form):
        # Выводим информацию о пароле перед ошибкой
        messages.error(self.request, 'Ошибка при вводе данных. Убедитесь, что вы выполнили все требования к паролю.')
        return super().form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        # Если пользователь уже авторизован, перенаправляем на главную страницу (или любую другую)
        if request.user.is_authenticated:
            return redirect('add_note_on_site:add_note')  # Замените 'home' на нужный URL или имя маршрута
        return super().dispatch(request, *args, **kwargs)

    

class LoginView(FormView):
    form_class = CustomLoginForm
    template_name = 'my_auth/login.html'
    success_url = reverse_lazy("add_note_on_site:add_note")

    def dispatch(self, request, *args, **kwargs):
        # Если пользователь уже авторизован, перенаправляем на главную страницу (или любую другую)
        if request.user.is_authenticated:
            return redirect('add_note_on_site:add_note')  # Замените 'home' на нужный URL или имя маршрута
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Неправильный логин или пароль')
            return self.form_invalid(form)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy('my_auth:login'))