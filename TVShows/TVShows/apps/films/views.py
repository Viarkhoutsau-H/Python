from django.shortcuts import render
from .models import Film, Genre, Comment, Actor, Mark
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

def index(request):
    films_list = Film.objects.order_by('year')
    return render(request, 'films/movies.html', {'films_list': films_list})


def detail(request, film_id):
    try:
        films = Film.objects.get(id=film_id)
    except:
        raise Http404("Фильма нет")

    return render(request, 'films/detail.html', {'film': films})


def comment(request, film_id):
    try:
        films = Film.objects.get(id=film_id)
    except:
        raise Http404("Фильма нет")

    films.comment_set.create(author=request.POST['name'], message=request.POST['text'])

    return HttpResponseRedirect(reverse('films:detail', args=(films.id,)))

