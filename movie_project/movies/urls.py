from django.urls import path
from .views import HomeView, UploadCSV, MovieListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload/', UploadCSV.as_view(), name='upload_csv'),
    path('api/movies/', MovieListView.as_view(), name='movie-list'),
]
