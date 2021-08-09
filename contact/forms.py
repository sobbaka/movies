from django import forms
from .models import Contact
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

class ContactForm(forms.ModelForm):
    """Форма подписки через email"""
    captcha = ReCaptchaField(score_threshold=0.5)
    class Meta:
        model = Contact
        fields = ('email', 'captcha', )
        widgets = {
            'email': forms.TextInput(attrs={
                'class':'editContent',
                'placeholder': 'Your email ...'
            }),

        }
        labels = {
            'email': ''
        }