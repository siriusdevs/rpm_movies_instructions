"""the movies views belong here."""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Filmwork, Person, Genre


def custom_main(req):
    """Renders request to custom index.html page."""
    film_works = Filmwork.objects.all().count()
    persons = Person.objects.all().count()
    genres = Genre.objects.all().count()

    return render(
        req,
        'index.html',
        context={'film_works':film_works,
                'persons':persons,
                'genres':genres},
    )

def main_page(req):
    """Just renders main.html page."""
    return render(req, 'main.html')

def render_dummy(req):
    """Returns simple http response."""
    return HttpResponse("<h1>This is the home page</h1>")

def redirection_page(req):
    """Redirects you elsewhere."""
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')