myFavoritMovies = [
    {
        "title": "Into the wild", 
        "year": 2015,
        "rating": 4,
        "description":"Into the wild opis"

    },
    {
        "title": "Sherlock Holmes", 
        "year": 2009,
        "rating": 4.3,
        "description":"Sherlock Holmes opis"

    },
      {
         "title": "Apocalypto", 
        "year": 2006,
        "rating": 4.1,
        "description":"Apocalypto opis"

    },
      {
         "title": "Skarb narodów", 
        "year": 2004,
        "rating": 4.0,
        "description":"Skarb narodów opis"

    }
]

print("Tytuł pierwszego filmu to: " + myFavoritMovies[0]["title"])
print("Rok premiery drugiego filmu to: " + str(myFavoritMovies[1]["year"]))
print("Ocena IMDB trzeciego filmu to: " + str(myFavoritMovies[2]["rating"]))
print("Krótki opis czwartego filmu to: " + myFavoritMovies[3]["description"])