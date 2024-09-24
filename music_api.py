import requests

# API credentials for Last.fm
API_KEY = "ef2fea58529c79073c5f40c3e68008fd"
API_URL = "http://ws.audioscrobbler.com/2.0/"

#API credentials for Spotify

# Get music recommendations from Last.fm or Spotify
def get_music_recommendation(artist_name):
    # API call to get recommendations based on the artist
    response = requests.get(f"{API_URL}artists/{artist_name}/recommendations", headers={
        "Authorization": f"Bearer {API_KEY}"
    })
    
    if response.status_code == 200:
        tracks = response.json()["tracks"]
        return [track['name'] for track in tracks]  # Return a list of recommended track names
    else:
        return ["No recommendations found."]
