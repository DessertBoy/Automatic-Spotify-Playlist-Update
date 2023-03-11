from AllMusicScraper import WebScraper
from Request_Options import Request_Methods
from Spotify_Access import SpotifyAccess
import random #Will be used to select random page numbers and random songs from an album
import time #Use to space out our Spotify POST request
import json #Need to use the method json.dumps() to update our Spotify playlist

"""

The two scopes we will be working with are playlist-read-private and playlist-modify-private.
Playlist-read-private allows us to read and access are playlist if it is private.
Playlist-modify-private allows us to modify (update) our private playlist

If you set your playlist to public you need to change your scopes to playlist-modify-public. Choose public scopes.

Here is a link explaining what Spotify scopes are: https://developer.spotify.com/documentation/general/guides/authorization/scopes/
"""

#Opening the text file that includes our username and password
f = open('Username_Password.txt','r')

file_content = f.read()
file_content = file_content.split()

"""
username: Spotify username
password: Spotify password
playlist_id: The ID of our playlist
playlist_url: The endpoint that we need to send our post request to in order to update our playlist with our new songs.

"""
username,password,playlist_id = file_content[1],file_content[3],file_content[5]
playlist_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

#-------------------------------------------------------------- Refresh Token/Authorization --------------------------------------------------------------------------------
def token_refresher():
	"""
	Every Spotify API endpoint requires token in order to be used/access. This function will automatically retrieve a new token for us in order to be able to udpate our playlist.
	Before retrieving a token you need to specify your scopes. To learn more about what a scope is please visit the Spotify API documentation.
	Our Spotify_Access class takes care of selecting our scopes for us. 

	Token/Authorization explanation: https://developer.spotify.com/documentation/general/guides/authorization/

	"""

	#Url where we can select our scoped and retrieve our new token.
	scope_token_url = 'https://developer.spotify.com/console/post-playlists/?user_id=&body=%7B%22name%22%3A%22New%20Playlist%22%2C%22description%22%3A%22New%20playlist%20description%22%2C%22public%22%3Afalse%7D'

	log_in = SpotifyAccess(username,password)
	log_in.retrieve_token(scope_token_url)
	token = log_in.token

	return token

#-------------------------------------------------------------- Retrive Song ID's from Playlist ----------------------------------------------------------------------

def retrieve_songid():
	"""
	Every song on Spotify has an ID assigned to it. Before we update our playlist we first want to get rid of all the songs that are currently in our playlist.
	This function will help us retrieve all the song ID's that are currently in our playlist. Once we have theose ID's we will be able to remove the songs from our playlist
	to update with new songs.

	API endpoint documentation can be found here:https://developer.spotify.com/documentation/web-api/reference/#/operations/get-playlists-tracks
	API endpoint for this function can be found here: https://developer.spotify.com/console/get-playlist-tracks/
	"""

	#Limit is the number of song ID's we want returned from our playlist.
	limit = {'limit':50}

	#The tracks that are currently in our playlist. Tracks will be returned in JSON format.
	playlist_tracks = Request_Methods.get(url = playlist_url, headers = headers, paramaters = limit)

	#Where our song IDs will be stored.
	song_ids = []

	#Retrieving song IDs.
	for i in range(len(playlist_tracks['items'])):
		#URI is the songs ID.
		song_ids.append({"uri":f"spotify:track:{playlist_tracks['items'][i]['track']['id']}"})

	return song_ids

#-------------------------------------------------------------- Remove Songs from Playlist ---------------------------------------------------------------------------

def song_removal(song_ids):
	"""
		This delete function will be used to delete the old songs that are in our playlist.
		The headers and paramaters need to be in the from of a dictionary.

		song_ids: A list of the song ID's to be removed.
		url: The url of our playlist.
		headers: Our headers are going to be our Authorization with our OAuth token.
		data: The song ID's of the songs we are trying delete from our playlist.

		API playlist track removal endpoint documentation can be found here: https://developer.spotify.com/documentation/web-api/reference/#/operations/remove-tracks-playlist
		API playlist track removal endpoint can be found here: https://developer.spotify.com/console/delete-playlist-tracks/
	"""

	param = {"tracks":song_ids}

	song_removal = Request_Methods.delete(url = playlist_url, headers = headers, data = param)


# #-------------------------------------------------------------------- Search For Songs --------------------------------------------------------------------------------
def album_search():
	"""
	This function will scrape random albums from the genre of our choice from allmusic.com.
	For this function it is highly recommended you understand basic HTML. By knowing basic 

	random_page_number: The page number our scrapper will scrape from.
	parser: The type of parser we will be using
	element: HTTP element
    class_name: name of the HTTP element class
    class_name2: name of the HTTP element class
	"""
	random_page_number = random.randint(1,10)
	print('\n')
	print(f'Page number {random_page_number} has been selected')
	url = f"https://www.allmusic.com/advanced-search/results/{random_page_number}"
	parser = "html.parser"
	element = "td"
	class_name = "title"
	class_name2 = "artist"

	#To change the headers you are going to have to go back to the website and inspect the page again, depending on the genre you want. You will find the filter in Inspect>Network>
	#On the search bar search for "results" and click on "results/". From there a window will pop up, click on the "Payload" tab, and click on "view source".
	genre_filter = "filters%5B%5D=%26subgenre%3DMA0000013621&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=" 


	headers = { 
    "host": "www.allmusic.com", 
    "connection": "keep-alive", 
    "accept": "text/html, /; q=0.01", 
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8", 
    "x-requested-with": "XMLHttpRequest", 
    "sec-ch-ua-mobile": "?0", 
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", 
    "origin": "https://www.allmusic.com", 
    "sec-fetch-site": "same-origin", 
    "sec-fetch-mode": "cors", 
    "sec-fetch-dest": "empty", 
    "referer": "https://www.allmusic.com/advanced-search", 
    "accept-encoding": "gzip, deflate, br",
     "accept-language": "en-US,en;q=0.9"} 

	 #Discography is where our list of albums will be saved.
	discography = WebScraper.scraper(url = url,headers = headers,genre_filter = genre_filter,parser = parser,element = element,class_name = class_name,class_name2 = class_name2)


	return discography

#-------------------------------------------------------------- Retrieve Album Uri --------------------------------------------------------------------------------

def retrieve_album_uri(discography):
	"""
	This function will help us retrieve the Spotify ID's of the albums we retrieved from allmusic.com. If the album is available on Spotify the ID will be added to our list. If it is not you will
	receive a message with the name of the artist and album that was not found.

	search_url: Spotify "Search" endpoint. This endpoint will help us search for the albums.
	album_ids = The album ID's that were returned from the album_search function.
	headers: Our headers are going to be our Authorization with our OAuth token.
	params: Request paramaters required. You can find the paramaters required in the Spotify search API documentation.
	search = Search results returned from our spotify search. Object will be a dictionary.

	API search endpoint documentation can be found here: https://developer.spotify.com/documentation/web-api/reference/#/operations/search
	API search endpoint can be found here: https://developer.spotify.com/console/get-search-item/
	"""

	search_url = "https://api.spotify.com/v1/search"
	album_ids = []


	for artist,album in discography.items():
		for name in album:
			try:
		 		params = {'q':f'artist:{artist} album:{name}','type':'album'}
		 		search = Request_Methods.get(url = search_url, headers = headers, paramaters = params)

		 		print(f"The album {search['albums']['items'][0]['name']} by {search['albums']['items'][0]['artists'][0]['name']} is available on Spotify")
		 		print('\n')

		 		album_ids.append(search['albums']['items'][0]['id'])
		 		time.sleep(2)

			except BaseException:
				print(f"The album {name} by {artist} is not available on Spotify")
				print('\n')
				pass

	return album_ids


# -------------------------------------------------------------- Retrieve Song Uri --------------------------------------------------------------------------------

def retrieve_songs(album_ids):
	"""
	This function will select random songs from the albums that were available on spotify from our allmusic.com search. Once the songs are selected,
	our playlist is will be updated with the new songs that were chosen.

	song_id = Where the ID's from the selected songs will be stored
	album_url: The endpoint that will return which songs are inside our selected albums
	params: Request paramaters required. You can find the paramaters required in the Spotify search API documentation.
	rand_indx = random number that will be selected between zero and the length of items returned in our "tracks" search.

	API album tracks search endpoint documentation: https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-albums-tracks
	API update playlist endpoint documentation: https://developer.spotify.com/documentation/web-api/reference/#/operations/add-tracks-to-playlist

	API album tracks search endpoint: https://developer.spotify.com/console/get-album-tracks/
	API update playlist endpoint: https://developer.spotify.com/console/post-playlist-tracks/


	"""
	print('Now I will proceed to choosing a random song from each of the albums listed above')
	print('\n')

	song_ids = []

	for ids in album_ids:
		try:
			
			album_url = f'https://api.spotify.com/v1/albums/{ids}/tracks'
			

			params = {'limit': 20}

			tracks = Request_Methods.get(url = album_url, headers = headers, paramaters = params)		

			rand_indx = random.randint(0,len(tracks['items'])-1)

			song_ids.append(tracks['items'][rand_indx]['id'])

			print(f"The song {tracks['items'][rand_indx]['name']} by {tracks['items'][rand_indx]['artists'][0]['name']} has been selected")
			print('\n')

			time.sleep(2)

		except BaseException as e:
			print("Looks like there was an error and the song that was next could not be retrieved")
			print(f'This was the erorr: {e}')
			print('\n')


	for ids in song_ids:

		print("I will now begin to update your playlist with the newly selected songs")
		print('\n')

		song_id = {'uris': [f'spotify:track:{ids}']}

		udpate_playlist = Request_Methods.post(url = playlist_url, headers = headers, data = json.dumps(song_id))

		print('Your playlist has been updated')


#-------------------------------------------------------------- Run Code --------------------------------------------------------------------------------



token = token_refresher()
headers = {'Authorization': f'Bearer {token}'}
playlist_song_ids = retrieve_songid()
song_removal(playlist_song_ids)
discography = album_search()
# album_ids = retrieve_album_uri(discography)
# retrieve_songs(album_ids)