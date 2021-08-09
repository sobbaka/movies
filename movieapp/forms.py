from django import forms
from .models import Reviews, Rating, RatingStar
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class ReviewForm(forms.ModelForm):
    """Добавление отзывов"""
    captcha = ReCaptchaField(score_threshold=0.5)
    class Meta:
        model = Reviews
        fields = ('parent', 'name', 'email', 'text', 'captcha')
        widgets = {
            "name": forms.TextInput(attrs={'class': "form-control border"}),
            "email": forms.EmailInput(attrs={'class': "form-control border"}),
            "text": forms.Textarea(attrs={'class': "form-control border"}),
        }


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
