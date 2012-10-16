from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from core.models import *
from core.forms import *

def index(request, template_name='index.html'):
    return _render_with_context(request, template_name, { })

def guestbook(request, template_name="guestbook.html"):
    guestbook_entrys = GuestbookEntry.get_all_entries()

    if request.method == 'POST': # If the form has been submitted...
        form = GuestbookEntryForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            form.save()
            return HttpResponseRedirect(reverse('core.views.guestbook')) # Redirect after POST
    else:
        form = GuestbookEntryForm() # An unbound form

    return _render_with_context(request, template_name, { 'form': form, 'guestbook_entrys' : guestbook_entrys })

def _render_with_context(request, url, vars):
   from django.template import RequestContext
   from django.shortcuts import render_to_response
   return render_to_response(url, vars, context_instance=RequestContext(request))
