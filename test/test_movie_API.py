import tmdbsimple as tmdb
tmdb.API_KEY = '093181dc8a621a849d2a4d9913814d91'
movie = tmdb.Movies(122906)
response = movie.info()
# overview for storyline
# title as title
response2 = movie.videos() 

print response['title']
print response

tv_show = tmdb.TV(53606)
response3 = tv_show.info()
# overview for storyline
# title as title
response4 = tv_show.videos() 

print response3['original_name']
print response4['results'][0]['key']
print response3
