from django.urls import path, include

from django_basics_retake.recipes.views import CatalogueRecipes, CreateRecipe, DetailRecipe, EditRecipe, DeleteRecipe

urlpatterns = (
    path("catalogue/", CatalogueRecipes.as_view(), name="catalogue"),
    path("create/", CreateRecipe.as_view(), name="create_recipe"),
    path(
        "<int:pk>/",
        include([
            path("details/", DetailRecipe.as_view(), name="detail_recipe"),
            path("edit/", EditRecipe.as_view(), name="edit_recipe"),
            path("delete/", DeleteRecipe.as_view(), name="delete_recipe"),
        ]),
    )
)