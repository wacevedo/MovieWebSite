import os

def get_API_KEY():
    current_dir = os.path.dirname(os.path.realpath('__file__'))
    API_KEY_value = open(current_dir+'\\tmdb_API_KEY.conf').read()
    return API_KEY_value
