from movie_rating_system import rating
from movie_rating_system import movie

def movie_date_and_time():
    from datetime import datetime
    date_time = datetime.now()
    hour = date_time.hour
    if hour > 12:
        hour = hour % 12
    elif hour == 0:
        hour = 12
    date_and_time = date_time.strftime(f"%d %m %Y  {hour}:%M %p")
    return date_and_time


def add_movie(title):
    # For adding a movie to the list
    movies.append({"name": title, "date": movie_date_and_time()})
    ratings.append([])

def remove_movie(title):
    count = 0
    for movie in movies:
        if movie["name"].lower() == title.lower():
            movies.remove(movies[count])
            ratings.remove(ratings[count])
        count += 1

def add_ratings(title, rating):
    counter = 0
    for movie in movies:
        if movie["name"].lower() == title.lower():
            ratings[counter].append(rating)
        counter += 1



movies = []
ratings = []

add_movie("Semi")
add_movie("Colon")
add_ratings("semi", 4.5)
add_ratings("semi", 4.0)
add_ratings("colon", 3.0)
print(movies)
print(ratings)
remove_movie("semi")
print(movies)
print(ratings)

rate = rating.Rating()
ratings = [rate.rating_list()]
movi = movie.Movie()
move = [{"name":"semi", "date":'12:3 pm'}, {"name":"colon", "date":'3:0 pm'}]

movi.add_movie("Semi")
movi.add_movie("Colon")
movi.add_movie("Coco")

for item in move:
    print(f"{item["name"]}")