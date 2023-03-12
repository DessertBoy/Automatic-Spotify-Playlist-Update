import requests
import json

"""
Creating a class with request methods that already returns the data in json format.
Didn't really need to create this module but did it anyways to avoid less lines of code in my main.py file.

"""

class Request_Methods:

	def get(url,headers = None,paramaters = None):

		"""
		This get function will be used to retrieve our spotify playlist and the songs in it.
		This function will also be used to search for the artist and album on Spotify.

		The headers and paramaters need to be a dictionary

		url: The url of our playlist.
		headers: Our headers is going to be our Authorization with our OAuth token.
		params: Paramaters specifying what we want from the get request. For retrieving songs from our playlist the paramaters will be the limit of the songs we want back.

		The paramaters for searching the artist and album on Spotify will include the name of the artist, the name of the album, and the "type". The "type" here would be the album.
		
		"""
		response = requests.get(url, headers = headers, params = paramaters)

		response_json = response.json()

		return response_json

	def post(url,headers = None,data = None):
		"""
		This post function will be used to update our playlist with new songs.

		The headers and paramaters need to be dictionary.

		url: The url used to search for songs in the Spotify API.
		headers: Our headers is going to be our Authorization with our OAuth token.
		data: The song ID's of the songs we are trying to update our playlist with.
		
		"""
		
		response = requests.post(url, headers = headers, data = data)

		return response

	def delete(url,headers = None,data = None):
		"""
		This delete function will be used to delete the old songs that are currently in our playlist.

		The headers and paramaters need to be a dictionary.

		url: The url of our playlist.
		headers: Our headers are going to be our Authorization with our OAuth token.
		data: The song ID's of the songs we are trying delete from our playlist.
		
		"""

		response = requests.delete(url, headers = headers, data = json.dumps(data))

		return response