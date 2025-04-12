import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from time import sleep

load_dotenv()

## ------------------------------------------------------------ Constants ------------------------------------------------------------ ##
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
USER_ID = os.getenv("USER_ID")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")

# Define the scope for permissions required
scope = "playlist-modify-public playlist-modify-private"

## ------------------------------------------------------------ Function to Refresh Spotify Token ------------------------------------------------------------ ##
def refresh_spotify_token():
    """Refresh the Spotify access token using the refresh token."""
    refresh_token_url = "https://accounts.spotify.com/api/token"
    refresh_token_headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    refresh_token_data = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    response = requests.post(url=refresh_token_url, headers=refresh_token_headers, data=refresh_token_data)
    refreshed_token_info = response.json()
    return refreshed_token_info.get("access_token")

## ------------------------------------------------------------ Function to Search for Tracks on Spotify ------------------------------------------------------------ ##
def search_track(song_title, access_token):
    """Search for a song on Spotify and return the track URI"""
    search_url = f"https://api.spotify.com/v1/search?q={song_title}&type=track&limit=1"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(search_url, headers=headers)
    data = response.json()

    if data['tracks']['items']:
        track_uri = data['tracks']['items'][0]['uri']
        return track_uri
    else:
        return None

## ------------------------------------------------------------ Function to Add Tracks to Playlist ------------------------------------------------------------ ##
def add_tracks_to_playlist(playlist_id, track_uris, access_token):
    """Add a list of track URIs to a Spotify playlist."""
    add_tracks_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    # Add the tracks in batches of 100 (API limitation)
    for i in range(0, len(track_uris), 100):
        track_batch = track_uris[i:i + 100]
        payload = {
            "uris": track_batch
        }
        response = requests.post(add_tracks_url, headers=headers, json=payload)
        if response.status_code == 201:
            print(f"Successfully added {len(track_batch)} tracks to the playlist.")
        else:
            print(f"Failed to add tracks. Error: {response.status_code}")
        sleep(1)  # Avoid hitting rate limits

## ------------------------------------------------------------ Function to Fetch Billboard Hot 100 ------------------------------------------------------------ ##
def fetch_billboard_songs(date):
    """Fetch Billboard Hot 100 songs for a given date."""
    billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
    }
    response = requests.get(url=billboard_url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    song_elements = soup.select("div ul li ul li h3")
    song_titles = [song.getText().strip() for song in song_elements]
    return song_titles, billboard_url

## ------------------------------------------------------------ Function to Create Spotify Playlist ------------------------------------------------------------ ##
def create_spotify_playlist(date, access_token):
    """Create a new Spotify playlist with the given date."""
    create_playlist_url = f"https://api.spotify.com/v1/users/{USER_ID}/playlists"
    playlist_data = {
        "name": f"Billboard Top 100 - {date.split('-')[0]}",
        "description": f"Top 100 songs from Billboard on {date}",
        "public": True
    }
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url=create_playlist_url, headers=headers, json=playlist_data)
    playlist_info = response.json()
    return playlist_info

## ------------------------------------------------------------ Main Function ------------------------------------------------------------ ##
def main():
    date = input("Enter the date (YYYY-MM-DD) for Billboard Hot 100 chart: ")
    song_titles, billboard_url = fetch_billboard_songs(date)
    
    print("Fetched songs for the date:", date)
    print("Go to:", billboard_url)
    print("Song Titles:", song_titles)

    # Refresh access token if needed
    global ACCESS_TOKEN
    if not ACCESS_TOKEN:
        ACCESS_TOKEN = refresh_spotify_token()

    # Create a playlist on Spotify
    playlist_info = create_spotify_playlist(date, ACCESS_TOKEN)
    playlist_url = playlist_info.get("external_urls", {}).get("spotify", "")
    if playlist_url:
        print(f"Playlist created! Access it here: {playlist_url}")
    else:
        print("Failed to create playlist.")

    # Search for tracks and add them to the playlist
    track_uris = []
    for song in song_titles:
        track_uri = search_track(song, ACCESS_TOKEN)
        if track_uri:
            track_uris.append(track_uri)
        else:
            print(f"Could not find track for: {song}")

    if track_uris:
        add_tracks_to_playlist(playlist_info['id'], track_uris, ACCESS_TOKEN)
    else:
        print("No tracks to add.")

## ------------------------------------------------------------ Calling the Main Function ------------------------------------------------------------ ##
if __name__ == "__main__":
    main()
