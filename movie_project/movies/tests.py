import os
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class MovieAPITestCase(APITestCase):

    def test_upload_csv(self):
        # Dynamically get the path to the CSV file in the same directory
        csv_file_path = os.path.join(os.path.dirname(__file__), 'movies_data_assignment.csv')
        
        # Upload a sample CSV file
        with open(csv_file_path, 'rb') as file:
            response = self.client.post(reverse('upload_csv'), {'file': file})
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_movies(self):
        response = self.client.get(reverse('movie-list'), {'page': 1, 'sort_by': 'release_date'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_by_language(self):
        response = self.client.get(reverse('movie-list'), {'language': 'en'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
