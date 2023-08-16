from pytube import YouTube, Search
import os
from pydub import AudioSegment
import math

def get_playlist(search_query):
    yt = Search(search_query).results[0]
    
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
    
    destination = '.'
    
    # download the file
    out_file = video.download(output_path=destination)
    
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    command = f'ffmpeg -i "{new_file}" -b:a 320k audio.mp3'
    os.system(command)
    os.remove(new_file)
    
    # result of success
    print(yt.title + " has been successfully downloaded.")

    sound = AudioSegment.from_mp3("audio.mp3")

    # len() and slicing are in milliseconds
    point = 115000
    playlist = []
    for i in range(int(math.floor(len(sound)/point))+1):
        playlist.append(sound[i*point:(i+1)*point])

    # writing mp3 files is a one liner
    for i in range(len(playlist)):
        playlist[i].export(f"output/{i+1}.mp3", format="mp3")
    os.remove("audio.mp3")