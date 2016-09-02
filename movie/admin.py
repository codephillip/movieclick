from django.contrib import admin

from movie.models import Movie, Category, Genre, MovieGenre, NotFoundMovie, FeedBack


class MovieAdmin(admin.ModelAdmin):
    model = Movie
    list_display = ('id', 'name', 'category', 'popularity', 'download_link', 'watch_link', 'trailer_link')


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('id', 'year')


class NotFoundMovieAdmin(admin.ModelAdmin):
    model = NotFoundMovie
    list_display = ('id', 'name', 'release_date')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre)
admin.site.register(MovieGenre)
admin.site.register(NotFoundMovie, NotFoundMovieAdmin)
admin.site.register(FeedBack)
