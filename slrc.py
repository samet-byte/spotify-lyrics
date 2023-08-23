import requests
import subprocess
import sys

def create_lrc_file(track, artist, lyrics):
    lrc_content = f"[ti:{track}]\n[ar:{artist}]\n\n" + lyrics

    with open(f"{artist} - {track}.lrc", "w") as lrc_file:
        lrc_file.write(lrc_content)

artist = ""
track = ""

current_arg = None

if len(sys.argv) > 1:

    for (i, arg) in enumerate(sys.argv):
        if arg == "-a":
            current_arg = "artist"
        elif arg == "-t":
            current_arg = "track"
        elif arg == "-h":
            print("Usage: python spotify_api.py [-a artist] [-t track]")
            exit()
        elif current_arg == "artist":
            artist += sys.argv[i] + " "
        elif current_arg == "track":
            track += sys.argv[i] + " "

    artist = artist.strip()
    track = track.strip()


else:
    artist = input("Artist : ")
    track = input("Track  : ")

track_id = subprocess.run(["python", "get_spotify_track_id_with_artist_title.py", artist, track], capture_output=True, text=True).stdout.strip()

api_url = f"https://spotify-lyric-api.herokuapp.com/?trackid={track_id}&format=lrc"
response = requests.get(api_url)
data = response.json()
lrc_lines = []

for line in data["lines"]:
    time_tag = line["timeTag"]
    words = line["words"]

    if time_tag and words:
        lrc_lines.append(f"[{time_tag}] {words}")

lrc_text = "\n".join(lrc_lines)

print(lrc_text)

create_lrc_file(track, artist, lrc_text)