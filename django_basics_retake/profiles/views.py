from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django_basics_retake.profiles.forms import CreateProfileForm, EditProfileForm
from django_basics_retake.profiles.models import Profile
from django.views import generic as views


# Create your views here.
def get_profile():
    return Profile.objects.first()

def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("catalogue")

    context = {
        "form": form,
        "no_nav": True,
    }

    return render(request, "profiles/create-profile.html", context)


class DetailProfile(views.DetailView):

    queryset = Profile.objects.all()
    template_name = 'profiles/details-profile.html'

    def get_object(self, queryset=None):
        return get_profile()

def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('detail_profile')
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profiles/edit-profile.html', context)


class DeleteProfileView(views.DeleteView):
    template_name = "profiles/delete-profile.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()