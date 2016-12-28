import tmdbsimple as tmdb

tmdb.API_KEY = '093181dc8a621a849d2a4d9913814d91'
base_img_url = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2'
base_youtube_url = 'https://www.youtube.com/watch?v='

def get_content(content):
    info = content.info()
    image = base_img_url + info['poster_path']
    storyline = info['overview']    
    video_response = content.videos() 
    video = base_youtube_url + video_response['results'][0]['key']
    content_value = (storyline, image, video)
    return content_value

def get_movie_info(id):
    movie = tmdb.Movies(id)
    content_value = get_content(movie)
    info = movie.info()
    title = info['title']
    runtime = int(info['runtime'])/60  #This is for convert the minutes to hours
    movie_value = (title, runtime) + content_value
    return movie_value

def get_tv_info(id):
    tv_show = tmdb.TV(id)
    content_value = get_content(tv_show)
    info = tv_show.info()
    title = info['original_name']
    number_of_seasons = info['number_of_seasons']
    number_of_episodes = info['number_of_episodes']
    tv_show_value = (title, number_of_seasons, number_of_episodes) + content_value
    return tv_show_value