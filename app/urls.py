# Django
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Views
from . import views

# App
app_name = 'app'

urlpatterns = [
    path('', views.index, name="index"),
    path('<slug:slug>/', views.film_detail, name="film_detail"),
    path('/films/', views.search_films, name="search_films"),
    path('path_views', views.path_views, name="path_views"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

