from tkinter import *
from api_setup import api_calling

BG_COLOR = "black"

root = Tk()
root.title("Spotify Playlist Generator")
root.config(padx=50, pady=50, bg=BG_COLOR)

canvas = Canvas(bg=BG_COLOR, highlightthickness=0, width=500, height=300)
canvas.grid(column=0, row=0, columnspan=3)

img = PhotoImage(file="image.gif")
canvas.create_image(250, 110, image=img)

date_text = Label(
    text="To what time would you like to travel to?\n(YYYY-MM-DD post 2020)",
    width=35,
    bg=BG_COLOR,
    fg="white",
)
date_entry = Entry(width=15, highlightthickness=0, borderwidth=1, bg= BG_COLOR)
date_entry.insert(END, "YYYY-MM-DD")

status_label = Label(text="", bg=BG_COLOR, fg="white", borderwidth= 1)

def on_button_click():
    date = date_entry.get()
    if date != "YYYY-MM-DD" and len(date) == 10:
        status_label.config(text="⏳ Creating your playlist...")
        try:
            api_calling(date)
            status_label.config(text="✅ Playlist created! Check your Spotify.")
        except Exception as e:
            status_label.config(text=f"❌ Error: {e}")
    else:
        status_label.config(text="⚠️ Please enter a valid date (YYYY-MM-DD).")

confirm_button = Button(
    text="Create Playlist",
    command=on_button_click,
    highlightthickness=0,
    borderwidth=0
)

date_text.grid(column=0, row=1)
date_entry.grid(column=1, row=1)
confirm_button.grid(column=2, row=1)
status_label.grid(column=0, row=2, columnspan=3, pady=10)

root.mainloop()
