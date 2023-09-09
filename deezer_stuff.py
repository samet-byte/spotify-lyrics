import subprocess
import sys
import requests

api_prefix = "https://api.deezer.com/search?q="
query = ""

def get_deezer_track_id_with_query(query):
    api_url = f"{api_prefix}{query}"
    print(api_url)
    response = requests.get(api_url)
    data = response.json()
    # print(data)
    # track_id = data["data"][0]["id"]
    track_link = data["data"][0]["link"]
    artist = data["data"][0]["artist"]["name"]
    track = data["data"][0]["title"]
    print(f"Artist: {artist}")
    print(f"Track: {track}")
    print(track_link)
    return [track_link, f"{artist} - {track}"]



def sanitize_command(command):
    # Check for parentheses in the command
    if '(' in command or ')' in command:
        # Escape parentheses with backslashes
        command = command.replace('(', '').replace(')', '')
    return command
def get_music(query):
    link_title = get_deezer_track_id_with_query(query)
    link = sanitize_command(link_title[0])
    title = sanitize_command(link_title[1])
    # subprocess.run(["python", "slrc.py", title], capture_output=True,text=True).stdout.strip()
    subprocess.run(f"rip url --max-quality 0 {link}", shell=True)


if len(sys.argv) > 2:
    for (i, arg) in enumerate(sys.argv):
        if i > 0:
            query += arg + " "
    query.strip()
else:
    query = input("Query : ")

get_music(query)