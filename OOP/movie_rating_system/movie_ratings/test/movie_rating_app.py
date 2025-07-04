from datetime import date

date = date.today()
year = date.year
month = date.month
day = date.day

def add_movie(title):
    #For adding a movie to the list
    movies.append({"name":title, "date":(year,month,day)})
    ratings.append([])

def rate_movie(title, rating):
    #For rating a movie
    for count in range(len(movies)):
        if movies[count]["name"] == title:
            ratings[count].append(rating)

def average_rating_for_each_movie(title):
    average = 0
    for count in range(len(movies)):
        if movies[count]["name"] == title:
            average = sum(ratings[count]) / len(ratings[count])
    return average

def average_ratings_for_all_movies():
    #To get average ratings for all movies
    average = 0
    for index in range(len(ratings)):
        average += sum(ratings[index]) / len(ratings[index])

    total_average = average / len(ratings)
    return float(f'{total_average:.1f}')

def movie_list():
    return movies

def rating_list():
    return ratings


movies = []
ratings = []
add_movie("The Prodigal")
print(movies[0]["name"], movies[0]["date"])


