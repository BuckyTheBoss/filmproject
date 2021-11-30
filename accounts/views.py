from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import RegistrationForm
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.


class SignupView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('homepage')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        self.object = form.save()
        Profile.objects.create(user=self.object)
        return super().form_valid(form)

    def form_invalid(self, form):
        # same as above
        print('form is invalid')
        return super().form_invalid(form)


class UserDetailView(DetailView):
    model = User
    template_name = 'accounts/profile.html'

    def get_object(self, queryset=None):
        # this will nullify the need for a pk in the url, by default get_object is the function in
        # detail views that requires a pk or slug
        return self.request.user
