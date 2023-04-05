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


@require_http_methods(['GET'])
def photo_reports(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'core/pages/photo_reports.html',
        context={
            'title': 'Фото-отчёты'
        }
    )


@require_http_methods(['GET'])
def photo_reports_detail(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'core/pages/photo_reports_detail.html',
        context={
            'title': 'Фото-отчёты'
        }
    )


@require_http_methods(['GET'])
def main_menu(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'core/pages/main_menu.html',
        context={
            'title': 'Главное меню'
        }
    )