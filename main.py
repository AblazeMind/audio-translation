from audio_to_srt import audio_srt
from video_to_audio import extract_audio
import os
from pathlib import Path

# assign directory
directory = 'video'
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    if filename == '.gitkeep':
        continue
    f = os.path.join(directory, filename)
    # file name without extension
    filename2=  Path(f).stem #os.path.splitext(f)[0]
    # extract audio
    extract_audio(f, filename2)
    #Convert to str
    audio_srt(f"audio/{filename2}.mp3", filename2) 

