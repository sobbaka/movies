from django import forms
from .models import Reviews

class ReviewForm(forms.ModelForm):
    """Добавление отзывов"""
    class Meta:
        model = Reviews
        fields = ('parent', 'name', 'email', 'text')