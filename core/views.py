from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def home(request: WSGIRequest) -> HttpResponse:
    ip = request.META['REMOTE_ADDR']
    return render(
        request,
        'core/pages/index.html',
        context={'ip_addr': ip, 'hello': f'Hello {ip}'}
    )