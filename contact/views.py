from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from .models import Contact
from .forms import ContactForm


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.POST.get('path'))
        return HttpResponseRedirect(request.POST.get('path'))