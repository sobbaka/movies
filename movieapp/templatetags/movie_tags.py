from django import template
from movieapp.models import Category, Movie

register = template.Library()

@register.simple_tag()
def get_categories():
    """Show all categories"""
    return Category.objects.all()


@register.simple_tag()
def get_latest_movies():
    """Show 3 latest movies"""
    return Movie.objects.all().order_by('id')[:3]