# Import moviepy
import moviepy.editor

# extract audio to mp3
def extract_audio(path, filename):

    #Load the Video Clip
    video = moviepy.editor.VideoFileClip(path)

    #Extract and export the Audio
    video.audio.write_audiofile(f"audio/{filename}.mp3")
    
    return "Done"

#extract_audio("video\Search in an almost sorted array  GeeksforGeeks.mp4", "Search in an almost sorted array  GeeksforGeeks")