from django.urls import path

from core.views import home, about, photo_reports, photo_reports_detail, main_menu

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('photos/reports/', photo_reports, name='photo_reports'),
    path('photos/reports/detail', photo_reports_detail, name='photo_reports_detail'),
    path('main/menu', main_menu, name='main_menu'),
]