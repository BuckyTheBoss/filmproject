from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import RegistrationForm, ProfileCreateForm, ProfileDataForm, ProfileSocialForm
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.


class SignupView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('homepage')
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['profile_form'] = ProfileCreateForm(self.request.POST or None)
        print(context)
        return context

    def form_valid(self, form):
        profile_form = ProfileCreateForm(self.request.POST)
        if profile_form.is_valid():
            self.object = form.save()
            profile = profile_form.save(commit=False)
            profile.user = self.object
            profile.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        # same as above
        print('form is invalid')
        return super().form_invalid(form)


class UserUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('my_profile')


    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['profile_form'] = ProfileDataForm(self.request.POST or None, instance=self.request.user.profile)
        context['social_form'] = ProfileSocialForm(self.request.POST or None, instance=self.request.user.profile)
        return context

    def get_object(self, queryset=None):
        # this will nullify the need for a pk in the url, by default get_object is the function in
        # detail views that requires a pk or slug
        return self.request.user

    def form_valid(self, form):
        # the kwarg instance=something  in the call to a modelform is imperative to having
        # the form update and object rather than create a new one
        social_form = ProfileSocialForm(self.request.POST, instance=self.request.user.profile)
        profile_form = ProfileDataForm(self.request.POST, self.request.FILES, instance=self.request.user.profile)
        forms = [social_form, profile_form]
        for other_form in forms:
            if not other_form.is_valid():
                return self.form_invalid(form)

        for other_form in forms:
            other_form.save()
        return super().form_valid(form)


def locked(request):
    if request.method == 'POST':
        if request.POST.get('code') == '12345':
            request.session['unlocked'] = True
            return redirect('homepage')
    return render(request, 'locked.html')