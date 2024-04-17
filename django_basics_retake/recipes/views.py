
from django.urls import reverse_lazy
from django.views import generic as views

from django_basics_retake.profiles.views import get_profile
from django_basics_retake.recipes.forms import RecipeForm
from django_basics_retake.recipes.models import Recipe


class CatalogueRecipes(views.ListView):
    queryset = Recipe.objects.all()
    template_name ='recipes/catalogue.html'

class CreateRecipe(views.CreateView):
    queryset = Recipe.objects.all()
    form_class = RecipeForm
    template_name ='recipes/create-recipe.html'
    success_url = reverse_lazy("catalogue")

    def form_valid(self, form):
        form.instance.author_id = get_profile().pk
        return super().form_valid(form)

class DetailRecipe(views.DetailView):
    queryset = Recipe.objects.all()
    template_name ='recipes/details-recipe.html'

class EditRecipe(views.UpdateView):
    queryset = Recipe.objects.all()
    form_class = RecipeForm
    template_name = 'recipes/edit-recipe.html'
    success_url = reverse_lazy("catalogue")

class DeleteRecipe(views.DeleteView):
    model = Recipe
    template_name = "recipes/delete-recipe.html"
    success_url = reverse_lazy("catalogue")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        context['title'] = recipe.title
        context['cuisine_type'] = recipe.cuisine_type
        context['ingredients'] = recipe.ingredients
        context['instructions'] = recipe.instructions
        context['cooking_time'] = recipe.cooking_time
        context['image_url'] = recipe.image_url
        return context