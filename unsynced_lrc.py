output_file_name = (input("Output file name : ") + ".lrc").strip()
lyrics = input("Lyrics : \n\n")

# create_lrc_file(lyrics)
def create_lrc_file(lyrics):
    lines = lyrics.split("\n")
    lrc_content = ""
    for line in lines:
        # lrc_content += [00.] line + "\n"