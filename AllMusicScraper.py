from bs4 import BeautifulSoup as bs
import requests


""" 
Creating a class to scrape albums and artist names from allmusic.com

bs4 documentation: https://beautiful-soup-4.readthedocs.io/en/latest/
requests documentation: https://requests.readthedocs.io/en/latest/user/quickstart/

"""

class WebScraper:

    def scraper(url,headers,genre_filter,parser,element= None, class_name = None, class_name2 = None):
        """
        url: The url of the website we will be scrapping
        headers: additional context and metadata about the request or response        
        genre_filter: filter that is used to search for the genre we are extracting music from
        parser: The variable that returns your data all "nice and clean"
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
