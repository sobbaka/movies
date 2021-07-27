from django.contrib import admin
from django.utils.safestring import mark_safe

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
@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} height="60">')

    get_image.short_description = "Изображение"

@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("id", "movie", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.shots.url} height="100">')

    get_image.short_description = "Изображение"


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('id', 'name')
    list_editable = ('url', )
    prepopulated_fields = {"url": ("name",)}
    search_fields = ('id', 'name',)

class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')

class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.shots.url} height="100">')

    get_image.short_description = "Изображение"

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'url', 'draft')
    list_display_links = ('id', 'name')
    list_filter = ('category', 'year', 'genres')
    search_fields = ('name', 'category__name', 'genres__name')
    list_editable = ('draft', )
    readonly_fields = ("get_image",)
    inlines = [MovieShotsInline, ReviewInline]
    save_on_top = True
    save_as = True
    filter_horizontal = ("directors", "actors", 'genres')
    fieldsets = (
        (None, {
            "fields": (('name', 'tagline'),)
        }),
        (None, {
            "fields": ("description", ("poster", "get_image"))
        }),
        (None, {
            "fields": ("year", "country")
        }),
        ("Actors and directors", {
            "classes": ("collapse",),
            "fields": (("directors", "actors"),)
        }),
        ("Extra", {
            "classes": ("collapse",),
            "fields": (
                ("genres", "category"),
                ("world_priemere", "budget", "fees_world")
                    )
                }),
        (None, {
            "fields": (("url", "draft"),)
        })
    )
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} height="200">')

    get_image.short_description = "Изображение"



@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'movie', 'parent')
    readonly_fields = ('name', 'email')

admin.site.register(Genre, GenreAdmin)
admin.site.register(RatingStar)
admin.site.register(Rating)

admin.site.site_title = 'My movie Site'
admin.site.site_header = 'My movie Site'