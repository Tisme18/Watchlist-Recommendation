from django.shortcuts import render
from .models import Movie
import heapq
from django.db.models import Q


# Create your views here.
def home(request):
    return render(request, 'finalproject/Homepage.html')

def movies(request):
    movies = list(Movie.objects.all())
    return render(request, 'finalproject/movie_details.html', {'movies': movies})

def findme(request):
    movies = Movie.objects.all()
    return render(request, 'finalproject/findme.html', {'movies': movies})

def binary_search(sortedlist, title):
  low = 0
  high = len(sortedlist) - 1

  while low <= high:
    mid = (low + high) // 2
    midmovie = sortedlist[mid]
    if midmovie == title:
        print(mid)
        return mid #returns the index of the movie
    elif midmovie < title:
      low = mid + 1
    else:
      high = mid - 1
  return -1

def findmovie(request):
    search_term = request.GET.get('searchmovie', '').strip()
    all_movies = Movie.objects.all().order_by('name')
    movie_titles = [movie.name for movie in all_movies]
    recos = []

    if search_term:
        index = binary_search(movie_titles, search_term)
        if index != -1:
            movie = all_movies[index]  # Retrieve the movie object
            movies = [movie]

            genre_list = [genre.strip() for genre in movie.genre.split(',')]
            direct = movie.director
            stars = [movie.stara, movie.starb, movie.starc, movie.stard]
            year = movie.year

            genre_list = list(set(genre_list))
            stars_list = list(set(stars))

            potential_recos = Movie.objects.exclude(pk=movie.pk).distinct()

            recos = []

            for potential in potential_recos:
                potential.match = 0

                potential_genres = [genre.strip() for genre in potential.genre.split(',')]
                potential.match += len(set(genre_list) & set(potential_genres))

                if potential.director == direct:
                    potential.match += 1

                potential_stars = [potential.stara, potential.starb, potential.starc, potential.stard]
                potential.match += len(set(stars_list) & set(potential_stars))

                if potential.year == year:
                    potential.match += 1

                heapq.heappush(recos, [potential.match, potential.imdb, potential.meta, potential.votes, potential.gross,  potential])  

                if len(recos) > 5:
                    heapq.heappop(recos)

            recos = [heapq.heappop(recos)[5] for _ in range(len(recos))]
            recos.reverse()
            print(recos)
        else:
            movies = []
    else:
        movies = all_movies

    return render(request, 'finalproject/findme.html', {'movies': movies, 'search_term': search_term, 'recos': recos})


def sort(request, by):    
    def mergesort(arr, key):
        if (len(arr)<=1):
            return arr; 
        else:
            midi = len(arr)//2 
            arrLeft = mergesort(arr[:midi], key)
            arrRight = mergesort(arr[midi:], key) 

        return merge(arrLeft,arrRight,key) 

    def merge(arrLeft,arrRight,key):
        c = []
        i = j = 0

        while i < len(arrLeft) and j < len(arrRight):
            if key(arrLeft[i]) <= key(arrRight[j]):
                c.append(arrLeft[i])
                i += 1           
            else:
                c.append(arrRight[j])      
                j += 1            

        c.extend(arrLeft[i:])
        c.extend(arrRight[j:])

        return c
    
    def key(movie):
        if by == 'name':
            return movie.name.lower() if movie.name else ""
        elif by == 'year':
            return movie.year or 0
        elif by == 'cert':
            return movie.cert.lower() if movie.cert else ""
        elif by == 'runtime':
            return movie.runtime or 0
        elif by == 'genre':
            return movie.genre.lower() if movie.genre else ""
        elif by == 'imdb':
            return -(movie.imdb or 0.0)
        elif by == 'meta':
            return -(movie.meta or 0)
        elif by == 'director':
            return movie.director.lower() if movie.director else ""
        elif by == 'artist':
            return (
                (movie.stara or "") + (movie.starb or "") + (movie.starc or "") + (movie.stard or "")
            ).lower()
        elif by == 'votes':
            return -(movie.votes or 0)
        elif by == 'gross':
            return -(movie.gross or 0.0)
        else:
            return ""
    
    allmovies = list(Movie.objects.all())
    sorted_movies = mergesort(allmovies, key)
    return render(request, 'finalproject/movie_details.html', {'movies': sorted_movies})






