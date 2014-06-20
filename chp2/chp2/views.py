from django.http import HttpResponse, Http404
from django.template import Template, Context, TemplateDoesNotExist
from django.template.loader import get_template
from django.shortcuts import render
import datetime

def request_viewer(request):
	html = "<html><body><pre> %s </pre></body></html>" % request
	return HttpResponse(html)

def hello(request):
    return HttpResponse("Hello world")

def hello_zeph(request):
    return HttpResponse("Hello there Zeph!!!!")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s GMT.</body></html>" % now
    return HttpResponse(html)

def current_datetime_template(request):
    t = Template("<html><body>It is now {{ d }} GMT.</body></html>")
    c = Context({"d": datetime.datetime.now()})
    return HttpResponse(t.render(c))

def current_datetime_template_file(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'d': now}))
    return HttpResponse(html)

def current_datetime_template_shortcut(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'d': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def intentional_error(request):
    #assert False
    raise StandardError('boo hoo')

def handle_vanilla_template(request, template, suffix):
	''' Go directly to the static (but inherited) template. No variables needed. '''
	try:
		return render(request, template, {'suffix' : suffix})
	except TemplateDoesNotExist as tdne:
		return request_viewer(request)
