from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView

from .forms import RegistrationForm, LoginForm
from django.utils.translation import gettext_lazy as _


class ClientRegistration(View):
    def setup(self, request, *args, **kwargs):
        super().setup(self, request, *args, **kwargs)

        request.title = _("Ro'yhatdan o'tish")

    def get(self, request):
        return render(request, 'layouts/form.html', {
            'form': RegistrationForm()
        })

    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            messages.success(request, _("Siz muvaqiyatli ro'yxatdan o'tdingiz"))

            return redirect('main:index')

        return render(request, 'client/registration.html', {
            'form': form
        })


class ClientLogin(View):
    def setup(self, request, *args, **kwargs):
        super().setup(self, request, *args, **kwargs)

        request.title = _("Tizimga kirish")

    def get(self, request):
        return render(request, 'layouts/form.html', {
            'form': LoginForm()
        })



    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)

                messages.success(request, _("{} Siz tizimga kirdingiz.) ".format(user.username)))

                return redirect('main:index')

            form.add_error('password', "Login va/yoki parrol noto'g'ri!")

        return render(request, 'client/login.html', {
            'form': form
        })

@login_required
def client_logout(request):
    messages.success(request, "Xayr {}!".format(request.user.username))
    logout(request)

    return redirect('main:index')


class ClientProfile(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'photo']
    template_name = "layouts/form.html"
    success_url = reverse_lazy('client:profile')

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = "Profile"
        request.button_title = "Saqlash"

    def get_object(self, queryset=None):
        return self.request.user