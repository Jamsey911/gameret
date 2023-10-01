"""
Imports for about views
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import ContactForm


def about(request):
    """
    view rendering contact form and
    send mail functionality
    """
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            user_message = form.cleaned_data['message']
            subject = form.cleaned_data['inquiry_purpose']
            message = render_to_string(
                'about/confirmation_email/email_confirmation.txt', {
                    'name': name,
                    'message': user_message
                })
            email_from = settings.DEFAULT_FROM_EMAIL
            email_to = [form.cleaned_data['email']]

            send_mail(
                subject,
                message,
                email_from,
                email_to
            )
            messages.success(request, 'Your message was sent successfuly')
            return redirect(reverse('about:about'))

        else:
            messages.error(request, 'An error occured please check the form')

    context = {
        'form': form,
    }
    return render(request, 'about/about.html', context)
