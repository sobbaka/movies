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


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'url', 'draft')
    list_display_links = ('id', 'name')
    list_filter = ('category', 'year', 'genres')
    search_fields = ('name', 'category__name', 'genres__name')
    list_editable = ('draft', )
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    filter_horizontal = ("directors", "actors", 'genres')
    fieldsets = (
        (None, {
            "fields": (('name', 'tagline'),)
        }),
        (None, {
            "fields": ("description", "poster")
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


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'movie', 'parent')
    readonly_fields = ('name', 'email')



admin.site.register(Actor)
admin.site.register(Genre, GenreAdmin)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Rating)
# admin.site.register(Reviews)