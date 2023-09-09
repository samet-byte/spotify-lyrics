import asyncio
import subprocess
import time
import os
from colorama import init, Fore


def parse_lrc(file_path):
    lyrics = []

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith("["):
                timestamp, text = line.split("]", 1)
                timestamp = timestamp[1:]  # Remove leading '['
                if timestamp[0].isdigit():
                    lyrics.append((timestamp, text))

    return lyrics



async def run_command(command):

    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate()
    return process.returncode, stdout, stderr


def play_music():
    command = "afplay x.mp3"
    asyncio.run(run_command(command=command))

def display_lyrics(lyrics):
    global total_seconds, prev_total_seconds
    init(autoreset=True)  # Initialize colorama



    for i, (timestamp, text) in enumerate(lyrics):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(Fore.CYAN + text)

        if i > 0:
            prev_timestamp = lyrics[i - 1][0]
            prev_minutes, prev_seconds = map(float, prev_timestamp.split(":"))
            prev_total_seconds = prev_minutes * 60 + prev_seconds
            time.sleep(total_seconds - prev_total_seconds)

        minutes, seconds = map(float, timestamp.split(":"))
        total_seconds = minutes * 60 + seconds

        if i == 0:
            time.sleep(total_seconds)  # Pause at the beginning
        else:
            time.sleep(total_seconds - prev_total_seconds)


def main():
    lrc_file = "example.lrc"  # Replace with your LRC file path
    lyrics = parse_lrc(lrc_file)
    # play_music()
    display_lyrics(lyrics)


if __name__ == "__main__":
    main()
