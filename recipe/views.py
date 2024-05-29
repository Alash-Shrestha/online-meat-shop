import re
from django.shortcuts import render, redirect
from django.contrib import messages

from recipe.models import *


# Create your views here.
def separate_sentences(paragraph):
    # Define regular expression pattern to match end of sentences
    sentence_end_pattern = r"(?<=[.!?]) +"

    # Split the paragraph into sentences using the pattern
    sentences = re.split(sentence_end_pattern, paragraph)

    return sentences

def recipe_list(request):
    if request.method == "POST":
        searchData = request.POST.get("search_product")
        if searchData != "":
            recipes = Recipe.objects.filter(name__icontains=searchData)
            if len(recipes) == 0:
                messages.warning(request, "Recipe Not Found")
                return redirect(request, "recipe:recipe_list")
            else:
                return render(request, "recipe/recipe_list.html", {"recipes": recipes})
    recipes = Recipe.objects.all()
    return render(request, "recipe/recipe_list.html", {"recipes": recipes})

def recipe(request, name):
    recipe = Recipe.objects.get(name=name)
    return render(request, "recipe/recipe.html", {"recipe": recipe})


def search_recipe(request):
    if request.method == "POST":
        searchData = request.POST.get("search_recipe")
        if searchData != "":
            recipes = Recipe.objects.filter(name__icontains=searchData)
            if len(recipes) == 0:
                messages.warning(request, "Recipe Not Found")
                return redirect("recipe:recipe_list")
            else:
                return render(request, "recipe/recipe_list.html", {"recipes": recipes})


def add_recipe(request):
    if request.method == "POST" and "image" in request.FILES:
        user = request.user
        username = user.username
        name = request.POST.get("title")
        image = request.FILES["image"]
        description = request.POST.get("description")
        ingredients = request.POST.get("ingredients")
        ingredients = separate_sentences(ingredients)
        instructions = request.POST.get("instructions")
        category_id = request.POST.get("category")
        category = Category.objects.get(id=category_id) if category_id else None

        recipe = Recipe.objects.create(
            user=user,
            username=username,
            name=name,
            image=image,
            category=category,
            description=description,
            instructions=instructions,
        )
        for ingredient in ingredients:
            ingredient = Ingredient.objects.create(name=ingredient)
            recipe.ingredients.add(ingredient)
        recipe.save()
        messages.success(request, "Recipe uploaded successfully. Wait for admin approval")
        return redirect("recipe:recipe_list")
    else:
        categories = Category.objects.all()
        return render(request, "recipe/add_recipe.html", {"categories": categories})


def my_recipe(request):
    user = request.user
    recipes = Recipe.objects.filter(user=user)
    return render(request, "recipe/my_recipe.html", {"recipes": recipes})
