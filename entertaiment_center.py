import media
import fresh_tomatoes
import media_getter

furious = media.Movie(*media_getter.get_movie_info(168259))
deadpool = media.Movie(*media_getter.get_movie_info(293660))
insidious = media.Movie(*media_getter.get_movie_info(49018))
now_you = media.Movie(*media_getter.get_movie_info(291805))
matrix = media.Movie(*media_getter.get_movie_info(603))
time = media.Movie(*media_getter.get_movie_info(122906))
love = media.Tv_Show(*media_getter.get_tv_info(53606))
vikings= media.Tv_Show(*media_getter.get_tv_info(44217))
walking = media.Tv_Show(*media_getter.get_tv_info(1402))

movies = [matrix, time, insidious, furious,
		  deadpool, now_you, love, vikings, walking]

fresh_tomatoes.open_movies_page(movies)
