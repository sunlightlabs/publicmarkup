from django import forms
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from postmark import PMMail
from publicmarkup.legislation.models import Legislation

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea())

# views

def index(request):
    legislation = Legislation.objects.filter(allow_comments=True)
    return render_to_response("legislation/legislation_list.html",
                              {'legislation': legislation},
                              context_instance=RequestContext(request))

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, label_suffix="")
        if form.is_valid():
            data = form.cleaned_data
            mailmsg = PMMail(
                subject='[PublicMarkup.org] contact from %s' % data['name'],
                text_body='%s <%s>\n\n%s' % (data['name'], data['email'], data['comment']),
                sender=settings.POSTMARK_SENDER,
                to=settings.POSTMARK_SENDER,
                reply_to=data['email'],
            )
            mailmsg.send()
            messages.success(request, "Thanks for contacting us. We'll get back to you shortly.")
            return HttpResponseRedirect('/')
    else:
        form = ContactForm(label_suffix="")
    return render_to_response("contact.html", {'form': form}, context_instance=RequestContext(request))

def signup(request):
    messages.success(request, "Thanks for signing up and getting involved in the transparency effort!")
    return HttpResponseRedirect('/')

def about(request):
    legislation = Legislation.objects.filter(allow_comments=False).order_by("-pk")
    return render_to_response("about.html", {'legislation': legislation}, context_instance=RequestContext(request))
