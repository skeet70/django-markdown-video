from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response

def markdown_parser(request):
   """Defines a parser for use with the preview option in markItUp!"""
   markup = request.POST.get('data', '')
   return render_to_response('markitup_preview.html',
      { 'preview': markup },
      context_instance=RequestContext(request))

