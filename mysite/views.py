
from django.shortcuts import render

from .forms import ContactForm


def _form_view(request, template_name='bootstrap4.html', form_class=ContactForm):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = form_class()
    return render(request, template_name, {'form': form})