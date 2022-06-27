from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect


from django.views.generic import View
from django.views.generic.edit import FormView

from .models import User

from .forms import UserRegisterForm, LoginUserForm


class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):

        User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password1'],

        )

        return super(UserRegisterView, self).form_valid(form)


class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginUserForm
    success_url = reverse_lazy('home_app:view-menu1')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
           reverse(
               'home_app:view-index'
           ) 
        )