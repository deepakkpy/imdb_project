# Django Movie API

This is a Django-based API for managing movie data, including functionality for uploading movie data via CSV, viewing a list of movies, and supporting filtering, sorting, and pagination of movie records.

## Features

- **Upload Movies via CSV**: POST a CSV file to populate the movies database.
- **List Movies**: Retrieve a list of movies with options for filtering, sorting, and pagination.
- **Admin Panel**: Easily manage movies via Django Admin.
  
## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Setup and Configuration](#setup-and-configuration)
4. [API Endpoints](#api-endpoints)
5. [Testing the APIs](#testing-the-apis)
6. [Contributing](#contributing)
7. [License](#license)

## Requirements

- Python 3.8+
- Django 3.2+
- PostgreSQL (or another database of your choice)
- pip (for installing dependencies)

## Installation

Follow the steps below to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/django-movie-api.git
   cd django-movie-api
2. Create a virtual environment:
   python -m venv venv
   
3. Activate the virtual environment:
  On Windows:
     venv\Scripts\activate
  On macOS/Linux:
      source venv/bin/activate
4.Install the required dependencies:
   pip install -r requirements.txt

5.Create a superuser: You need a superuser to access the Django Admin:
   python manage.py createsuperuser
   
6.Run the server: Finally, run the development server:
    python manage.py runserver
The API should now be accessible at http://127.0.0.1:8000/.

Setup and Configuration
Configure the Database:
If you're using PostgreSQL, make sure you have created a database in PostgreSQL and configured the connection in settings.py.

Environment Variables:
It's a good practice to manage sensitive information (like database credentials, secret keys) in environment variables. You can use libraries like python-decouple to load these variables.

API Endpoints
The API supports the following endpoints:

1.POST /api/upload/ - Upload Movies via CSV
Description: Upload a CSV file containing movie data.
Request:

*Method: POST
*Body: Form-data with key file (CSV file).
Response:
*Status: 201 Created if successful.
Example response:

      {
        "message": "Movies successfully uploaded."
      }
GET /api/movies/ - List Movies
Description: Retrieve a list of movies with pagination, filtering, and sorting options.
Query Parameters:

*page: (optional) Page number for pagination.
*language: (optional) Filter by language (e.g., en, fr).
*release_year: (optional) Filter by release year.
*sort_by: (optional) Field to sort by (e.g., release_date, title).
Response:
*Status: 200 OK if successful.
Example response:

                {
                  "count": 100,
                  "next": "http://127.0.0.1:8000/api/movies/?page=2",
                  "previous": null,
                  "results": [
                    {
                      "title": "Movie Title",
                      "release_date": "2022-01-01",
                      "language": "en",
                      "rating": 8.5
                    },
                    ...
                  ]
                }


Testing the APIs

You can test the APIs using Postman or through automated tests.

1. Using Postman (Manual Testing)
   
    Postman Collection: Download and import the Postman collection for easy API testing. You can export your collection from Postman and share the .json file or provide the link to your collection.
(https://api.postman.com/collections/39690690-d450603f-cf7b-4522-85e5-a6d2a6418793?access_key=PMAT-01JCN6G1GBYWGGSY587X11HAN5)


*Example POST request to /api/upload/:
      Method: POST
      URL: http://127.0.0.1:8000/api/upload/
      Body: Form-data with key file and select the CSV file.
      
*Example GET request to /api/movies/:
  Method: GET
  URL: http://127.0.0.1:8000/api/movies/?page=1&language=en&sort_by=release_date

  
2. Automated Testing with Django
You can write integration tests for your API endpoints using Django’s TestCase.




        from rest_framework.test import APITestCase
        from rest_framework import status
        from django.urls import reverse
        
        class MovieAPITestCase(APITestCase):
    
                def test_upload_csv(self):
                    # Upload a sample CSV file
                    with open('movies_data_assignment.csv', 'rb') as file:
                        response = self.client.post(reverse('movie-upload'), {'file': file})
                        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            
                def test_get_movies(self):
                    response = self.client.get(reverse('movie-list'), {'page': 1, 'sort_by': 'release_date'})
                    self.assertEqual(response.status_code, status.HTTP_200_OK)
            
                def test_filter_by_language(self):
                    response = self.client.get(reverse('movie-list'), {'language': 'en'})
                    self.assertEqual(response.status_code, status.HTTP_200_OK)

Run the tests using:

python manage.py test


Contributing

We welcome contributions to improve this project.

1.Fork this repository.

2.Create a new branch for your feature or bugfix.

3.Make your changes and commit them with clear messages.

4.Push your changes to your forked repository.

5.Submit a pull request to the main repository.
