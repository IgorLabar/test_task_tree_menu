from django.contrib import admin
from .models import Category, Movie
from django_mptt_admin.admin import DjangoMpttAdmin

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Movie, MovieAdmin)


class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)