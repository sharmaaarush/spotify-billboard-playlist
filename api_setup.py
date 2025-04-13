## ------------------------------------------------------------ Imports ------------------------------------------------------------ ##
import os
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
load_dotenv()


## ------------------------------------------------------------ Constants ------------------------------------------------------------ ##
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
USER_ID = os.getenv("USER_ID")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")

scope = "playlist-modify-public playlist-modify-private"


# ------------------------------------------------------------ Spotify Token Refresh  ------------------------------------------------------------ ##
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
refresh_response = requests.post(url=refresh_token_url, headers=refresh_token_headers, data=refresh_token_data)
refreshed_token_info = refresh_response.json()
ACCESS_TOKEN = refreshed_token_info.get("access_token")


# ------------------------------------------------------------ Search for Track ------------------------------------------------------------ ##
def search_track(song_title, access_token):
    search_url = f"https://api.spotify.com/v1/search?q={song_title}&type=track&limit=1"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(search_url, headers=headers)
    data = response.json()

    if data['tracks']['items']:
        return data['tracks']['items'][0]['uri']
    else:
        return None


# ------------------------------------------------------------ Add Tracks ------------------------------------------------------------ ##
def add_tracks_to_playlist(playlist_id, track_uris, access_token):
    add_tracks_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    track_data = {"uris": track_uris}
    response = requests.post(add_tracks_url, headers=headers, json=track_data)

    if response.status_code == 201:
        print(f"✅ Successfully added {len(track_uris)} tracks to the playlist.")
    else:
        print(f"❌ Failed to add tracks. Error: {response.status_code}")


# ------------------------------------------------------------ Main Function ------------------------------------------------------------ ##
def api_calling(date):
    billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url=billboard_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    song_elements = soup.select("div ul li ul li h3")
    song_titles = [song.getText().strip() for song in song_elements]
    print(f"🎵 Billboard Top 100 on {date}:\n", song_titles)
    print("🔗 Go to:", billboard_url)

    # Create a Spotify playlist
    create_playlist_url = f"https://api.spotify.com/v1/users/{USER_ID}/playlists"
    playlist_data = {
        "name": f"Billboard Top 100 - {date.split("-")[0]}",
        "description": f"Top 100 songs from Billboard on {date}",
        "public": True
    }
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.post(url=create_playlist_url, headers=headers, json=playlist_data)
    playlist_info = response.json()

    playlist_url = playlist_info.get("external_urls", {}).get("spotify", "")
    if playlist_url:
        print(f"✅ Playlist created: {playlist_url}")
    else:
        print("❌ Failed to create playlist.")

    # Search tracks and add to playlist
    track_uris = []
    for song in song_titles:
        track_uri = search_track(song, ACCESS_TOKEN)
        if track_uri:
            track_uris.append(track_uri)
        else:
            print(f"⚠️ Could not find track: {song}")

    if track_uris:
        add_tracks_to_playlist(playlist_info['id'], track_uris, ACCESS_TOKEN)
    else:
        print("⚠️ No tracks to add.")


# ------------------------------------------------------------ Run standalone ------------------------------------------------------------ ##
if __name__ == "__main__":
    user_date = input("Enter date (YYYY-MM-DD): ")
    api_calling(user_date)
