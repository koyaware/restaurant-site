from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def home(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'core/pages/index.html',
        context={
            'title': 'Главная страница'
        }
    )


@require_http_methods(['GET'])
def about(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'core/pages/about.html',
        context={
            'title': 'О нас'
        }
    )