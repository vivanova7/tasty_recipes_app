from django.urls import path

from django_basics_retake.profiles.views import create_profile, DetailProfile, edit_profile, \
    DeleteProfileView

urlpatterns = (
    path("create/", create_profile, name="create_profile"),
    path("details/", DetailProfile.as_view(), name="detail_profile"),
    path("edit/", edit_profile, name="edit_profile"),
    path("delete/", DeleteProfileView.as_view(), name="delete_profile"),
)