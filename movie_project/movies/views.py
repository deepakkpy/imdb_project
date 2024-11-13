from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer
from .services import DataParser, MovieQueryService, PaginatorService
from io import TextIOWrapper
import csv

class HomeView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the Movie API!"}, status=status.HTTP_200_OK)

class UploadCSV(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        csv_file = TextIOWrapper(file.file, encoding='utf-8')
        reader = csv.DictReader(csv_file)
        movies = []
        
        for row in reader:
            try:
                movie = Movie(
                    title=DataParser.truncate_to_max_length(row['title']),
                    budget=DataParser.parse_decimal(row['budget']),
                    homepage=DataParser.truncate_to_max_length(row['homepage']),
                    original_language=row['original_language'],
                    original_title=DataParser.truncate_to_max_length(row['original_title']),
                    overview=DataParser.truncate_to_max_length(row['overview']),
                    release_date=DataParser.parse_date(row['release_date']),
                    revenue=DataParser.parse_decimal(row['revenue']),
                    runtime=row['runtime'],
                    status=row['status'],
                    vote_average=DataParser.parse_decimal(row['vote_average']),
                    vote_count=int(float(row['vote_count'])) if row['vote_count'] else 0,
                    production_company_id=row['production_company_id'],
                    genre_id=row['genre_id'],
                    languages=DataParser.truncate_to_max_length(row['languages'])
                )
                movies.append(movie)
            except ValueError as e:
                return Response({"error": f"Invalid data format: {e}"}, status=status.HTTP_400_BAD_REQUEST)

        Movie.objects.bulk_create(movies)
        return Response({"message": "CSV uploaded successfully"}, status=status.HTTP_201_CREATED)

class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.all()

        # Apply filters using MovieQueryService
        release_year = request.query_params.get('release_year')
        language = request.query_params.get('language')
        movies = MovieQueryService.filter_movies(movies, release_year, language)

        # Apply sorting using MovieQueryService
        sort_by = request.query_params.get('sort_by')
        movies = MovieQueryService.sort_movies(movies, sort_by)

        # Apply pagination using PaginatorService
        page_number = request.query_params.get('page', 1)
        page_obj = PaginatorService.paginate(movies, page_number, page_size=10)

        # Serialize data
        serializer = MovieSerializer(page_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
