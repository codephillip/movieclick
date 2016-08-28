from django.contrib import admin

from movie.models import Movie, Category


class MovieAdmin(admin.ModelAdmin):
    model = Movie
    list_display = ('id', 'name', 'category', 'popularity', 'download_link', 'watch_link')


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('id', 'year')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)
