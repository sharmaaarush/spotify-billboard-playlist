# 🎧 Spotify Playlist Creator from Billboard Hot 100

This Python project allows you to automatically create a Spotify playlist from Billboard's Hot 100 chart for any given date (after 2020). Using the Spotify API and BeautifulSoup for web scraping, it searches for the top 100 songs from the specified date, adds them to a new Spotify playlist, and shares the playlist URL with you.

## 📚 Table of Contents
- [📌 Project Overview](#-project-overview)
- [🛠️ Prerequisites](#-prerequisites)
- [⚙️ Setup](#-setup)
- [🔐 How to Access Credentials](#-how-to-access-credentials)
- [🚀 How to Use](#-how-to-use)
- [🧠 Functions](#-functions)
- [📄 License](#-license)
- [🙌 Credits](#-credits)

## 📌 Project Overview

The main goal of this project is to create a Spotify playlist based on the Billboard Hot 100 chart for any specific date. The process includes:

1. Fetching the Billboard Hot 100 for the given date  
2. Searching for the corresponding songs on Spotify  
3. Creating a new playlist on Spotify  
4. Adding the songs to the created playlist  
5. Providing the URL to access the playlist  

## 🛠️ Prerequisites

Before running the project, make sure you have:

- Python 3.x installed  
- `pip` for installing dependencies  
- A Spotify Developer Account for API credentials  
- Billboard Hot 100 data available (works for any date after 2020)  

### 📦 Required Python Packages

Install the required packages with:

```bash
pip install requests beautifulsoup4 python-dotenv
```

## ⚙️ Setup

### 📁 Clone the Repository

```bash
git clone https://github.com/your-username/spotify-playlist-from-billboard.git
cd spotify-playlist-from-billboard
```

### 📝 Create a .env File

In the project root, create a `.env` file and add the following environment variables:

```
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
REDIRECT_URI=your_redirect_uri
ACCESS_TOKEN=your_access_token
USER_ID=your_spotify_user_id
REFRESH_TOKEN=your_refresh_token
```

### ✅ Install the Required Dependencies

```bash
pip install -r requirements.txt
```

## 🔐 How to Access Credentials

### 🧑‍💻 Spotify Developer Account

To get the required credentials (`CLIENT_ID`, `CLIENT_SECRET`, and `USER_ID`):

- Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)  
- Create a new app to get your `CLIENT_ID` and `CLIENT_SECRET`  
- Set your `REDIRECT_URI`  
- Use Spotify’s Authorization Flow to get your `ACCESS_TOKEN` and `REFRESH_TOKEN`  

### 🛡️ Set Up `.env` File

Store your credentials in the `.env` file as shown above.

## 🚀 How to Use

### ▶️ Run the Application

```bash
python main.py
```

### 📆 Provide a Date

You’ll be prompted to enter the date in the format `YYYY-MM-DD` (after 2020) to get the Billboard Hot 100 for that date.

### 🔗 Get the Playlist Link

After processing, the script will create a playlist and print the Spotify playlist URL.

## 🧠 Functions

### 🔍 `search_track(song_title, access_token)`

**Description**: Searches for a song on Spotify and returns the track URI.  
**Parameters**:
- `song_title`: The name of the song  
- `access_token`: The current Spotify access token  
**Returns**: The URI of the song on Spotify or `None` if not found.

---

### 🎯 `add_tracks_to_playlist(playlist_id, track_uris, access_token)`

**Description**: Adds a list of track URIs to a Spotify playlist.  
**Parameters**:
- `playlist_id`: The ID of the playlist  
- `track_uris`: A list of track URIs to be added  
- `access_token`: The current Spotify access token

---

### 🧩 `main()`

**Description**: The main function that orchestrates fetching the Billboard Hot 100, creating the playlist, and adding tracks.

## 📄 License

This project is licensed under the MIT License.

## 🙌 Credits

Built with ❤️ by Aarush Sharma  
Inspired by Spotify API integration and Python automation practices.
