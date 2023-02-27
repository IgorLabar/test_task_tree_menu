from django.shortcuts import render
from django.views.generic import ListView
from .models import Movie, Category


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'


class MovieByCategory(ListView):
    context_object_name = 'movies'
    template_name = 'movie_list.html'
    
    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Movie.objects.filter(category=self.category)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.category
        return context