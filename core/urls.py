from django.urls import path

from core.views import home, about, photo_reports, photo_reports_detail, main_menu, bar_menu

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('photos/reports/', photo_reports, name='photo_reports'),
    path('photos/reports/detail', photo_reports_detail, name='photo_reports_detail'),
    path('menu/main', main_menu, name='main_menu'),
    path('menu/bar', bar_menu, name='bar_menu'),
]