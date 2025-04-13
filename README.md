# 🎧 Spotify Playlist Creator from Billboard Hot 100 (GUI Version)

![Spotify](image.gif)

This project allows you to automatically create a Spotify playlist based on the Billboard Hot 100 chart for any date after 2020 using a simple graphical interface (GUI). It integrates:

- 🎨 `tkinter` for a modern and interactive interface  
- 🧼 `BeautifulSoup` to scrape Billboard songs  
- 🎵 `Spotify's Web API` to search tracks and create playlists on your account  

---

## 📌 Project Overview

### 💡 What It Does:
- Opens a GUI window asking for a date (`YYYY-MM-DD`)  
- Scrapes Billboard Hot 100 chart for that date  
- Authenticates with Spotify using your credentials  
- Searches those songs on Spotify  
- Creates a new **private** playlist in your account  
- Adds all the matched songs to it  
- Gives you the **link to the Spotify playlist**  

So you get a Spotify playlist that reflects the top songs from any day in music history (post-2020).

---

## 🛠️ Prerequisites

### ✅ Installed Software:
- Python 3.x  
- Pip package manager  

### ✅ Required Python Packages:
Install them using:

```bash
pip install requests beautifulsoup4 python-dotenv
```

---

## ⚙️ Project Setup

### 📁 Clone the Repo
```bash
git clone https://github.com/your-username/spotify-playlist-from-billboard
cd spotify-playlist-from-billboard
```

### 📷 Assets
Keep the `image.gif` file in the project folder. It is used as a background image in your GUI.

---

### 🔐 Environment Variables (Sensitive Info)

Create a `.env` file and paste your Spotify credentials like this:

```
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
REDIRECT_URI=http://localhost:8888/callback
ACCESS_TOKEN=your_access_token
REFRESH_TOKEN=your_refresh_token
USER_ID=your_spotify_user_id
```

📝 You can get these credentials by creating an app on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

---

## 🧠 Project Structure and Files

```
spotify-playlist-from-billboard/
│
├── gui.py              # GUI logic using tkinter
├── main.py             # Core playlist creation flow
├── api_setup.py        # Spotify API authentication and token refresh
├── image.gif           # GIF used in the GUI
├── .env                # Environment variables (credentials)
└── README.md           # Project documentation
```

---

## 🖼️ GUI: What the User Sees

When you run the project:

```bash
python main.py
```

A GUI window appears with:

- A date input field  
- A "Create Playlist" button  
- A fancy background animation (`image.gif`)  

After entering a valid date (e.g., `2022-08-01`) and clicking the button, it:

- Scrapes the Billboard Top 100 songs for that day  
- Logs in to your Spotify account  
- Searches for matching songs  
- Creates a playlist and adds the found songs  
- Displays a confirmation with the playlist name and link in the terminal  

---

## 🧠 What Each File Does

### 🔹 `gui.py`
- Handles GUI using tkinter  
- Loads and displays a background GIF  
- Collects the user input (date)  
- Triggers playlist creation when the button is clicked  

### 🔹 `main.py`
- Orchestrates the overall flow  
- Connects the GUI to the backend  
- Calls functions from `api_setup.py` and uses scraped data to:
  - Search tracks on Spotify  
  - Create a new playlist  
  - Add the tracks  

### 🔹 `api_setup.py`
- Handles Spotify API Authorization  
- Gets fresh access tokens using refresh tokens  
- Contains:
  - `get_access_token()`  
  - `create_playlist()`  
  - `search_track()`  
  - `add_tracks_to_playlist()`  

---

## 🔐 How to Get Spotify Credentials

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Log in and create a new app  
3. Copy your:
   - `CLIENT_ID`
   - `CLIENT_SECRET`
4. Set `REDIRECT_URI` to: `http://localhost:8888/callback`
5. Use a tool/tutorial to get:
   - `ACCESS_TOKEN`
   - `REFRESH_TOKEN`
6. Find your `USER_ID` in your Spotify profile link

Paste everything in the `.env` file as shown earlier.

---

## 🚀 How to Run

- Ensure your `.env` file and `image.gif` are present  
- Open terminal inside the project folder  
- Run:

```bash
python main.py
```

🎉 A window opens — enter your date, hit "Create Playlist"  
⌛ Wait a few seconds  
🔗 Playlist link appears in your terminal  

---
