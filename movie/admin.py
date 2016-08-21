from django.contrib import admin

from movie.models import Movie, Category


class MovieAdmin(admin.ModelAdmin):
    model = Movie
    list_display = ('id', 'name', 'category', 'link', 'image')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Category)
