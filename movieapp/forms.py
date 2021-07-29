from django import forms
from .models import Reviews, Rating, RatingStar

class ReviewForm(forms.ModelForm):
    """Добавление отзывов"""
    class Meta:
        model = Reviews
        fields = ('parent', 'name', 'email', 'text')

class RatingForm(forms.ModelForm):
    """Форма добавления отзывов"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(),
        widget=forms.RadioSelect(),
        empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star", )
