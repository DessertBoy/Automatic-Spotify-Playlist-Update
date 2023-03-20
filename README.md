# Automatic Spotify Playlist Update
This project will automatically delete songs from any playlist that you have created on Spotify and it will upload new random songs from albums scraped from allmusic.com. However, it is recommended that you create a new playlist for this project.

This is a personal project. I decided to share it with the public in case anybody would like to create something similar and is looking for a reference or base.
I have included links to the documentation for the libraries I used and I've also included Youtube links to videos that helped me create this project.

You must use Spotify credentials to log in. That means not using Facebook, Apple, or Google to log in. I apologize for the inconvience if you use any of the three services listed above to log in. Hopefully in the future I'm able to update this project so anybody can log in regardless of the service they use to log in to their Spotify account. 

By default, this project is set to scrape Deep House albums from allmusic.com. In a video below I will show you how to get the genre ID from allmusic.com in case you want to scrape albums from a different genre :).

# Requirements
1. Have basic/intermediate knowledge of Python.
<br />

2. Basic knowledge of HTML

<br />

3. You will need to have Selenium, a webdriver for your browser, and Beautiful Soup installed. I will not get into details on how to install these packages, you can google that, but I will include Youtube links below on Selenium. Selenium could be confusing at first.
![image](https://user-images.githubusercontent.com/56139759/224896679-57e6ee97-8b22-49d0-99fc-fb3479a54573.png)
![image](https://user-images.githubusercontent.com/56139759/224896734-50e0081d-c209-4fd6-8f3e-a7baa24c4f4c.png)

<br />

4. You must have a Spotify account. You also need to create a Spotify Developer account which you can create [here](https://developer.spotify.com/dashboard/). It is free, all you need to do is log in and accept the Spotify Developer Terms of Service. You do not need to create a dashboard to continue with this project.

https://user-images.githubusercontent.com/56139759/224590136-492cd03a-c980-4ffa-b9f0-3598c2d8432b.mp4

<br />

5. This is not a requirement but I highly recommend creating a new playlist. The video below will show you how to get the playlist ID, also known as the Spotify URI. You simply click on the three dots underneath the playlist cover, go to Share, hover over "Copy link to playlist", and press Ctrl. A new option titled "Copy Spotify URI" will appear. Copy that and paste it as your playlist_id on the syntax. Make sure to get rid of the "spotify:playlist:" portion of the ID. Watch the video below to see  what I mean.

https://user-images.githubusercontent.com/56139759/224603757-cffc0833-2b25-4651-a841-9cc062f52665.mp4

<br />

6. You are going to have to decide whether you want to make your playlist public or private. This project by default has private scopes selected. If you decide to make your playlist public you are going to have to comment out playlist_modify_private and playlist_modify_private.click() and uncomment playlist_modify_public and playlist_modify_public.click(). P.S. Had to reduce video quality to be able to attach it.


https://user-images.githubusercontent.com/56139759/224895650-e561fb4d-6d98-4f90-8828-05658b2fe09d.mp4

<br />

# Resources

The video below will demonstrate how to obtain the genre ID for any genre on allmusic.com


https://user-images.githubusercontent.com/56139759/226225000-f4def5eb-88c7-4b15-a325-20c008345d26.mp4

<br />

Here are some links to some helpful youtube videos that go more into detail about selenium:
* [How to install selenium](https://www.youtube.com/watch?v=mvJ1dNHH3vM&list=PLL34mf651faPOf5PE5YjYgTRITzVzzvMz&index=5)
* [How to install webdriver](https://www.youtube.com/watch?v=z-biUumQxlw&list=PLL34mf651faPOf5PE5YjYgTRITzVzzvMz&index=8)
* [Webdriver_manager explanation and installation](https://www.youtube.com/watch?v=Z3M2GBu8t_k&list=PLL34mf651faPOf5PE5YjYgTRITzVzzvMz&index=11)
* [Explanation of web elements (will help understand the function driver.find_element)](https://www.youtube.com/watch?v=tQ-Vip-ySRg&list=PLL34mf651faPOf5PE5YjYgTRITzVzzvMz&index=57)
* [How to find XPATH and explanation of XPATH](https://www.youtube.com/watch?v=mKM35Hnsd5c&list=PLL34mf651faPOf5PE5YjYgTRITzVzzvMz&index=60)
