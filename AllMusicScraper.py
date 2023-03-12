from bs4 import BeautifulSoup as bs
import requests

""" 
The wesbite we are scrapping music from (allmusic.com) is an AJAX website. We will need to send a post request straight to the database where this website retrieves its data from.

In order to find the headers for the POST request we need to right click on the page after you've selected a genre (https://www.allmusic.com/advanced-search) and select Inspect > Network.
Once you are in the Networks section, in the search bar search for "results" and you will get a list of requests (if nothing appears refresh the page or click on your genre with the Network tab open). 

To find the genre header, search for your request by searching "results" in the Network search bar, and click on your "results" request. Once you click on your request a new window will appear. It will have the
headers of "Header", "Payload", "Preview", "Response", "Initiator", "Timing", and "Cookies". To find the genre header click on "Payload". A window will open up that looks like this:
*filters[]: some ID
*filter[]: The rest of the ID (this is a continuation of the first filters [])
*sort:

Go ahead and click on the column next to it, "view source", and the element there will be your filter payload for the type of genre you want to scrape. Copy that and paste it as the payload variable in the
main.py file.

The last thing you need to do is copy the headers from "Request Headers". You will be using these headers when you send out your request. We are extracting the data from the same source All Music imports it's data from.
The only headers that I use are "host", "connection","accept","content-type","x-requested-with","sec-ch-ua-mobile","user-agent","origin","sec-fetch-site","sec-fetch-mode","sec-fetch-dest","referer", "accept-encoding", and
"accept-language".
"""

""" Creating a class to scrape the HTML content"""

class WebScraper:

    def scraper(url,headers,genre_filter,parser,element= None, class_name = None, class_name2 = None):
        """
        url: The url of the website we will be scrapping
        headers: additional context and metadata about the request or response        
        genre_filter: filter that is used to search for the genre we are extracting music from 
        element: HTTP element
        class_name: name of the HTTP element class
        class_name: name of the HTTP element class
        """
        artist_album = {}

        s = requests.Session()

        response = s.post(url, data=genre_filter, headers=headers)

        soup = bs(response.content,parser)

        titles = soup.find_all(element,class_name)
        artist = soup.find_all(element,class_name2)


        for i in range(len(titles)):
            try:
                if artist[i].contents[1].contents[0] in artist_album.keys():
                    artist_album[artist[i].contents[1].contents[0]].append(titles[i].contents[1].contents[0])
                else:
                    artist_album[artist[i].contents[1].contents[0]] = [titles[i].contents[1].contents[0]]
            except:
                print('We do not include artists with the name "Various Artists"')


        return artist_album
