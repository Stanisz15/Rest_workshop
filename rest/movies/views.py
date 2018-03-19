from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView, Response
from movies.serializer import MovieSerializer, PersonSerializer
from movies.models import Movie, Person


class MoviesView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieView(APIView):
    def get(self, request, id):
        movie = get_object_or_404(Movie, pk=id)
        serializer = MovieSerializer(movie, context={'request': request})
        return Response(serializer.data)

    def delete(self, request, id):
        movie = get_object_or_404(Movie, pk=id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        movie = get_object_or_404(Movie, pk=id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PersonsView(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonView(APIView):
    def get(self, request, id):
        person = get_object_or_404(Person, pk=id)
        serializer = PersonSerializer(person, context={'request': request})
        return Response(serializer.data)

    def delete(self, request, id):
        person = get_object_or_404(Person, pk=id)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        person = get_object_or_404(Person, pk=id)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)