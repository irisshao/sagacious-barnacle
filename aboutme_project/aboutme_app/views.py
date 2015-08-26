# Create your views here.

# From Chapter 3. Django Basics (Tango with Django)
# from django.http import HttpResponse

# def index(request):
# 	return HttpResponse("Hello world!")

from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	# Request the context of the request
	context = RequestContext(request)

	# Construct a dictionary to pass to the template engine as its context.
	context_dict = {'boldmessage': "I am bold font from the context"}

	#Return a rendered response to send to the client.
	return render_to_response('aboutme_app/index2.html', context_dict, context)

def about(request):
	# Request the context of the request
	context = RequestContext(request)

	# Construct a dictionary to pass to the template engine as its context.
	context_dict = {'boldmessage': "I am bold font from the context"}

	#Return a rendered response to send to the client.
	return render_to_response('aboutme_app/about.html', context_dict, context)

def resume(request):
	# Request the context of the request
	context = RequestContext(request)

	# Construct a dictionary to pass to the template engine as its context.
	context_dict = {'boldmessage': "I am bold font from the context"}

	#Return a rendered response to send to the client.
	return render_to_response('aboutme_app/resume.html', context_dict, context)