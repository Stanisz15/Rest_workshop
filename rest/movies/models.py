from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    description = models.TextField(null=True)


class Movie(models.Model):
    title = models.TextField()
    description = models.TextField(null=True)
    director = models.ForeignKey(Person, related_name='directory', on_delete=models.CASCADE)
    starring = models.ManyToManyField(Person, through='PersonMovie')
    year = models.IntegerField()


class PersonMovie(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=128, null=True)