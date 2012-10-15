from django.shortcuts import render_to_response

def index(request, template_name='index.html'):
    return _render_with_context(request, template_name, { })

def guestbook(request, template_name="guestbook"):
    return _render_with_context(request, template_name, { })

def _render_with_context(request, url, vars):
   from django.template import RequestContext
   from django.shortcuts import render_to_response
   return render_to_response(url, vars, context_instance=RequestContext(request))
