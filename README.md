# spotify-lyrics

## Spotify Synced Lyrics (.lrc) Extractor

This is a script for extracting synchronized lyrics from Spotify tracks.

Heroku API from @akashrchandran/spotify-lyrics-api

## Usage

You can use the script by running the following command:

```bash
# SYNCED LYRICS
python slrc.py -a Pink Floyd -t Wish You Were Here
# DOWNLOAD MUSIC
python deezer_stuff.py DESIRED MUSIC WITH ANY FORMAT
python deezer_stuff.py Wish You Were Here Pink Floyd
```

The script will then search for the track on Spotify and extract the lyrics from the first result.

## Requirements
```bash
pip install -r requirements.txt
```

## Output

### Pink Floyd - Wish You Were Here.lrc

```
[ti:Wish You Were Here]
[ar:Pink Floyd]
[00:05.53] And disciplinary remains mercifully
[00:08.19] Yes and um, I'm with you Derek, this star nonsense
[00:11.98] Yes, yes
[00:12.57] Now which is it?
[00:13.65] I am sure of it
[00:16.13] ♪

...

[02:37.65] ♪
[03:15.79] How I wish, how I wish you were here
[03:22.37] We're just two lost souls
[03:25.09] Swimming in a fish bowl
[03:27.74] Year after year
[03:31.80] Running over the same old ground
[03:35.51] What have we found?
[03:37.99] The same old fears
[03:41.71] Wish you were here
```


