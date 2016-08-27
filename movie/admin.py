from django.contrib import admin

from movie.models import Movie, Category


class MovieAdmin(admin.ModelAdmin):
    model = Movie
    list_display = ('id', 'name', 'category', 'download_link', 'watch_link')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Category)
