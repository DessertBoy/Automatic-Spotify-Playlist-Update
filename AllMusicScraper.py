from bs4 import BeautifulSoup as bs
import requests

""" 
The wesbite we are scrapping music from (All Music) is an AJAX website. We will need to send a post request straight to the database where this website retrieves it's data from.

In order to find the headers for the POST request we need to right click on the page select Inspect > Network.
Once you are in the Networks section, in the search bar search for results and you will get a list of request. If you want to look for your genres payload the easiest thing to do would be to
click on your genre and look at the new request that shows up. If you already clicked on your request and are unsure which request it was, just unclick it and click again. 

To find the genre header, search for your request by searching "results" in the Network search bar, and click on your result request. Once you click on your request a new window will appear. It will have the
headers of "Header", "Payload", "Preview", "Response", "Initiator", "Timing", and "Cookies". To find the gengre header click on "Payload". There you will a page with the Form Data column selected, it will look like this:
*filter: some numbers
*filter: some number (this is a continuation of the filter)
*sort:
Go ahead and click on the column next to it, "view source", and the element there will be your filter payload for the type of genre you want to scrape. Copy that and paste as the payload variable in the
All Music Update.py file.

The last thing you do is copy the headers from "Request Headers". You will be using these headers when you send out your request. We are extracting the data from the same source All Music imports it's data from.
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
