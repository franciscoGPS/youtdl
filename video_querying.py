import filesystem_tools as fs
from youtube_search import search_first_video_id, get_authenticated_service
import make_table as mt


client = get_authenticated_service()
OPENMODE = "r"
FILENAME = "songs_query_names"
APPEND_MODE = "a"
FILENAME_WITH_VIDEO_IDS = "songs_query_names_and_youtube_ids"


#Object used to store the ids
filesystem = fs.Filesystem(FILENAME, OPENMODE)
file_to_save = fs.Filesystem(FILENAME_WITH_VIDEO_IDS, APPEND_MODE)


array_of_songs_to_query = []
array_of_songs_to_query = filesystem.file_to_list()


array_of_ids_to_query = list()

print("len(array_of_songs_to_query): ", len(array_of_songs_to_query))
for i in range(len(array_of_songs_to_query)):
	try:
   	    video_id = search_first_video_id(client, part='snippet', maxResults=1, q=array_of_songs_to_query[i][0], type='video')
   	    if (video_id != ""):
   	    	array_of_ids_to_query.append( array_of_songs_to_query[i][0] + ", "+ video_id)
   	    else:
   	    	print("song not found ", array_of_songs_to_query[i], i)	
	except IndexError as err:
		#ipdb.set_trace()
		print("song not found ", array_of_songs_to_query[i], i, err)
	
	#video_id = response['items'][0]['id']['videoId']

	#ipdb.set_trace()
	#file_to_save.save_default(array_of_songs_to_query[i])



mt.make_ids_table(FILENAME_WITH_VIDEO_IDS, array_of_ids_to_query)





"""
search_first_video(client, 
    part='snippet',
    maxResults=1,
    q='el triste jose jose',
    type='video')

"""