from fresh_tomatoes import open_movies_page
from media import Movie, Tv_Show
from media_getter import get_movie_info, get_tv_info

movie_ids = [168259, 293660, 49018, 291805, 603, 122906]
tv_show_ids = [53606, 44217, 1402]

open_movies_page([Movie(*get_movie_info(i)) for i in movie_ids] + 
				 [Tv_Show(*get_tv_info(i)) for i in tv_show_ids])
