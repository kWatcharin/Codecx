
from django.shortcuts import render
from django.http import HttpResponseRedirect

from general_app.forms import ContactMessageForm


def about_us(request):

    form = ContactMessageForm()
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect('contact_sending_status')
        
    context = {
        'form': form,
    }
    return render(request, 'general_app/about_us.html', context)


def contact_sending_status(request):

    return render(request, 'general_app/all_ready_sent_contact.html')