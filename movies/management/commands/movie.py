import csv
import os

import imdb

from movies.models import Movie


class MovieToDB:
    """
    class used for insert
    Movies on DB
    """

    def __init__(
        self,
        title,
        year,
        plot,
        category,
        director,
        cast,
        country
    ):
        self._title = title
        self._year = year
        self._plot = plot
        self._category = category
        self._director = director
        self._cast = cast
        self._country = country

    @staticmethod
    def load():
        """
        Load CSV file
        """
        path = os.path.dirname(os.path.abspath(__file__))
        file = open(path + '/imdb_movies.csv')
        reader = csv.reader(file)
        next(reader)
        return reader

    @staticmethod
    def parse(csv_file):
        """
        Parse CSV file and get data we need
        (title, year, plot, category, director,
        cast, country, picture)
        """
        list_objects = list()
        for row in csv_file:
            list_objects.append(MovieToDB.get(
                row[2],
                row[3],
                row[13],
                row[5],
                row[9],
                row[12],
                row[7]
            ))
        return list_objects

    @staticmethod
    def get(title,
            year,
            plot,
            category,
            director,
            cast,
            country):
        """
        Instanciate movie object
        """
        return MovieToDB(
            title,
            year,
            plot,
            category,
            director,
            cast,
            country
        )

    def display(self):
        """
        display movies in readable way
        """
        print(f"""
            ===========================
            title: {self._title}
            year: {self._year}
            plot: {self._plot}
            category: {self._category}
            director: {self._director}
            cast: {self._cast}
            country: {self._country}
            ===========================
        """)

    @staticmethod
    def get_picture():
        """
        get picture link from imdb python wrapper
        """
        ia = imdb.IMDb()
        movies = Movie.objects.all().values('title', 'year', 'picture')
        for movie in movies:
            if movie['picture'] is None:
                print(f"{movie['title']} hasn't a picture")
                try:
                    imdb_search = ia.search_movie(movie['title'])
                    for results in imdb_search:
                        if 'year' in results.keys():
                            if results['year'] == movie['year']:
                                picture = MovieToDB.get_picture_imdb(
                                    results.getID()
                                )
                                MovieToDB.insert_picture_to_db(
                                    picture,
                                    movie['title'],
                                    movie['year']
                                )
                except Exception:
                    pass
            else:
                print(f"{movie['title']} picture ==> OK")

    def _get_title(self):
        return self._title

    def _get_year(self):
        return self._year

    def _get_plot(self):
        return self._plot

    def _get_category(self):
        return self._category

    def _get_director(self):
        return self._director

    def _get_cast(self):
        return self._cast

    def _get_country(self):
        return self._country

    title = property(_get_title)
    year = property(_get_year)
    plot = property(_get_plot)
    category = property(_get_category)
    director = property(_get_director)
    cast = property(_get_cast)
    country = property(_get_country)
