from pytube import YouTube

 # where to save 
SAVE_PATH = "video/" #to_do 
  
# link of the video to be downloaded 
link="LINK_TO_VIDEO"
  
try: 
    # object creation using YouTube
    # which was imported in the beginning 
    yt = YouTube(link) 
except: 
    print("Connection Error") #to handle exception 
  
try: 
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(SAVE_PATH)
except: 
    print("Some Error!") 
print('Task Completed!') 