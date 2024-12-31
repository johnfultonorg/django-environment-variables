from django.shortcuts import render
from .forms import ContactForm
from .models import ContactMessage
import os
from django.conf import settings
from dotenv import load_dotenv


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data (e.g., save to a database or send an email)
            cleaned_data = form.cleaned_data

            if form.is_valid():
                ContactMessage.objects.create(**form.cleaned_data)

            print(cleaned_data)  # Example processing
            # Redirect to a thank-you page
            return render(request, 'contact/thank_you.html', {'name': cleaned_data["name"]})
    else:
        form = ContactForm()
        
        #os environment variable
        if 'SAMPLE_SYSTEM_VARIABLE' in os.environ:
            print(os.environ['SAMPLE_SYSTEM_VARIABLE'])
            os_variable = os.environ['SAMPLE_SYSTEM_VARIABLE']
        else:
            os_variable = ''
        
        #django setting variable
        if settings.SAMPLE_DJANGO_SETTINGS_VALUE:
            print(settings.SAMPLE_DJANGO_SETTINGS_VALUE)
            settings_variable = settings.SAMPLE_DJANGO_SETTINGS_VALUE
        else:
            settings_variable = ''
       
        #.env variable
        load_dotenv()
        print( os.getenv('SAMPLE_DOT_ENV_VALUE'))
        dot_env_variable = os.getenv('SAMPLE_DOT_ENV_VALUE')
        
        context = {'os_variable': os_variable,
                   'settings_variable': settings_variable,
                   'dot_env_variable': dot_env_variable,
                   'form': form
                   }
        return render(request, 'contact/contact.html', context)
