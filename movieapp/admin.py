from django.contrib import admin
from .models import (
    Category,
    Actor,
    Genre,
    Movie,
    MovieShots,
    RatingStar,
    Rating,
    Reviews
)
# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}

admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)