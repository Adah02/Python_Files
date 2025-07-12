from movie_rating_system import movie
from movie_rating_system import rating

movie_menu = '''
    Welcome to Epic Movie Rating System!
    press:-
    1 -> Add movie
    2 -> Rating
    3 -> View average movie rating
    4 -> View average ratings
    5 -> Remove movie from list
    6 -> Remove all from list
    7 -> View movie list & ratings
    8 -> Exit
    '''

print(movie_menu)
while True:
    movi = movie.Movie()
    rate = rating.Rating()
    movie_ = ''
    choice = int(input('Enter your choice: '))
    match choice:
        case '1':
            movie_ = input('Enter movie name: ')
            movi.add_movie(movie_)
        case '2':
            movie_ = input('Enter movie name: ')
            rating_ = input('Enter movie rating: ')
            rate.rate_movie(movie_, rating_)
        case '3':
            movie_ = input('Enter movie name: ')
            print(f"{movie_} {rate.average_rating_for_movie(movie_)}")
        case '4':
            movie_ = input('Enter movie name: ')
            print(f"{movie_} {rate.average_ratings_for_all_movies()}")
        case '5':
            movie_ = input('Enter movie name: ')
            movi.remove_movie(movie_)