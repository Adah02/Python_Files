from movie_rating_system import movie_rating
movi = movie_rating.Movie()

movie_menu = '''
    =================================
    Welcome to Epic Movies
    =================================
    press:-
    ---------------------------------
    1 -> Add movie
    2 -> Rating
    3 -> View average movie rating
    4 -> Remove movie from list
    5 -> View movie list & ratings
    6 -> Exit
    =================================
    '''
print(movie_menu)
while True:
    movie_ = ''
    choice = input('Enter your choice: ')
    match choice:
        case '1':
            movie_ = input('Enter movie name: ')
            movi.add_movie(movie_)
            print(f"{movie_} was added successfully!...")
        case '2':
            movie_ = input('Enter movie name: ')
            rating_ = input('Enter movie rating: ')
            movi.rate_movie(movie_, rating_)
        case '3':
            print(movi.average_rating_for_movie())
        case '4':
            movie_ = input('Enter movie name: ')
            movi.remove_movie(movie_)
        case '5':
            movi.movie_list_and_ratings()
        case '6':
            print('Goodbye!...')
            break
        case _:
            print('Sorry, try another option')