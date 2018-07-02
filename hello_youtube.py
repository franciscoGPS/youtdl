import urllib.request
import filesystem_tools as fs 
import ipdb as bp;
string_url = "https://www.googleapis.com/youtube/v3/search"
youtube_video_id_url = "https://www.youtube.com/watch?v="
video_id = "fNFzfwLM72c"
contents = urllib.request.urlopen(youtube_video_id_url + video_id).read()
#print(contents)
#youtube-dl -g "https://www.youtube.com/watch?v=fNFzfwLM72c"
OPENMODE = "a"
FILENAME = "youtube_video_id"

#Object used to store the ids
filesystem = fs.Filesystem(FILENAME, OPENMODE)
for x in range(0, 3):
	string = "We're oasdasdn time " + str(x) + "\n" 
	
#	bp.set_trace()
	filesystem.save_default( string )
    