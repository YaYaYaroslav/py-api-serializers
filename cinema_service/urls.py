from django.contrib import admin
from django.urls import path

from cinema.views import MovieSessionViewSet

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/cinema/movie_sessions/', MovieSessionViewSet.as_view({'get': 'list'}), name='movie_sessions'),
    path('api/cinema/movie_sessions/<int:pk>/', MovieSessionViewSet.as_view({'get': 'retrieve'}),
         name='movie_session_detail'),

]
