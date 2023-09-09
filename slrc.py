import os

import requests
import subprocess
import sys

ANSI_RESET = "\u001B[0m"
# ANSI_BOLD = "\u001B[1m"
# ANSI_ITALIC = "\u001B[3m"
# ANSI_UNDERLINE = "\u001B[4m"
# ANSI_COLOR_BLACK = "\u001B[30m"
# ANSI_COLOR_RED = "\u001B[31m"
# ANSI_COLOR_GREEN = "\u001B[32m"
# ANSI_COLOR_YELLOW = "\u001B[33m"
# ANSI_COLOR_MAGENTA = "\u001B[35m"
# ANSI_COLOR_CYAN = "\u001B[36m"
ANSI_COLOR_WHITE = "\u001B[37m"
# color_list = [ANSI_COLOR_RED, ANSI_COLOR_GREEN, ANSI_COLOR_YELLOW, ANSI_COLOR_MAGENTA, ANSI_COLOR_CYAN]

RESET = "\033[0m"
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Bright ANSI color codes
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# Background color codes (regular and bright)
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"
BG_BRIGHT_BLACK = "\033[100m"
BG_BRIGHT_RED = "\033[101m"
BG_BRIGHT_GREEN = "\033[102m"
BG_BRIGHT_YELLOW = "\033[103m"
BG_BRIGHT_BLUE = "\033[104m"
BG_BRIGHT_MAGENTA = "\033[105m"
BG_BRIGHT_CYAN = "\033[106m"
BG_BRIGHT_WHITE = "\033[107m"


color_list = [
    # RED, GREEN, YELLOW, MAGENTA, CYAN,
              BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_MAGENTA, BRIGHT_CYAN, BRIGHT_WHITE,
# BG_RED, BG_GREEN, BG_YELLOW, BG_MAGENTA, BG_CYAN, BG_BRIGHT_RED, BG_BRIGHT_GREEN, BG_BRIGHT_YELLOW, BG_BRIGHT_MAGENTA, BG_BRIGHT_CYAN
]


# def create_lrc_file(track, artist, lyrics):
def create_lrc_file(query, lyrics):
    regarding = "https://open.spotify.com/track/" + track_id
    # lrc_content = f"[ti:{track}]\n[ar:{artist}]\n[re:{regarding}]\n\n" + lyrics
    lrc_content = f"[re:{regarding}]\n\n" + lyrics

    folder_path = "lyrics"
    if not os.path.exists(folder_path): os.makedirs(folder_path)

    folder_path = "/Users/sametbayat/StreamripDownloads"

    file_name = f"{query}.lrc"
    full_file_path = os.path.join(folder_path, file_name)

    with open(full_file_path, 'w') as file:
        file.write(lrc_content)


query = ""

current_arg = None

if len(sys.argv) > 2:

    for (i, arg) in enumerate(sys.argv):
        if i == 0: continue
        query += arg + " "
    query.strip()

    # for (i, arg) in enumerate(sys.argv):
    #     if arg == "-a":
    #         current_arg = "artist"
    #     elif arg == "-t":
    #         current_arg = "track"
    #     elif arg == "-h":
    #         print("Usage: python slrc.py [-a artist] [-t track]")
    #         exit()
    #     elif current_arg == "artist":
    #         artist += sys.argv[i] + " "
    #     elif current_arg == "track":
    #         track += sys.argv[i] + " "
    #
    # artist = artist.strip()
    # track = track.strip()

else:
    query = input("Query : ")
    # artist = input("Artist : ")
    # track = input("Track  : ")

# track_id = subprocess.run(["python", "get_spotify_track_id_with_artist_title.py", artist, track], capture_output=True, text=True).stdout.strip()
track_id = subprocess.run(["python", "get_spotify_track_id_with_artist_title.py", query], capture_output=True,
                          text=True).stdout.strip()

api_url = f"https://spotify-lyric-api.herokuapp.com/?trackid={track_id}&format=lrc"
response = requests.get(api_url)
data = response.json()
# print(data)
if data["error"]:
    print("Stg went wrong! Better check the query!")
    exit()
lrc_lines = []

for line in data["lines"]:
    time_tag = line["timeTag"]
    words = line["words"]

    if time_tag and words:
        lrc_lines.append(f"[{time_tag}] {words}")

lrc_text = "\n".join(lrc_lines)

# print(ANSI_COLOR_CYAN + lrc_text + ANSI_RESET)
os.system('clear')

for line in lrc_lines:
    line_parts = line.split("]")
    print(ANSI_COLOR_WHITE+line_parts[0]+"] "+color_list[lrc_lines.index(line) % len(color_list)] + line_parts[1] + ANSI_RESET)
print()

create_lrc_file(query, lrc_text)
# create_lrc_file(track, artist, lrc_text)
