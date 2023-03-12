from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

"""
I will not get into detail over the functions I imported from selenium.
The selenium documentation can be found here: https://www.selenium.dev/documentation/

Here are some links to some helpful youtube videos that go more into detail about selenium:
* How to install selenium: https://www.youtube.com/watch?v=mvJ1dNHH3vM&list=PLL34mf651faPOf5PE5YjYgTRITzVzzvMz&index=5
* How to install webdriver: https://www.youtube.com/watch?v=z-biUumQxlw&list=PLL34mf651faPOf5PE5YjYgTRITzVzzvMz&index=8
* webdriver_manager explanation and installationn: https://www.youtube.com/watch?v=Z3M2GBu8t_k&list=PLL34mf651faPOf5PE5YjYgTRITzVzzvMz&index=11
* Explanation of web elements (will help understand the functions driver.find_element):https://www.youtube.com/watch?v=tQ-Vip-ySRg&list=PLL34mf651faPOf5PE5YjYgTRITzVzzvMz&index=57
* How to find XPATH and explanation of XPATH: https://www.youtube.com/watch?v=mKM35Hnsd5c&list=PLL34mf651faPOf5PE5YjYgTRITzVzzvMz&index=60


The scope we will be working is playlist-modify-private.

Playlist-modify-private allows us to modify (update) our private playlist

If you set your playlist to public you need to change your scopes to playlist-modify-public.

Here is a link explaining what Spotify scopes are: https://developer.spotify.com/documentation/general/guides/authorization/scopes/

"""


"""Creating a class with a method to automate the token refresh process"""

class SpotifyAccess:
	def __init__(self,username,password):
		"""
		self.token: Where the OAuth token to update our playlist will be saved
		self.username: Your spotify username
		self.password: Your spotify password
		"""
		self.token = None
		self.username = username
		self.password = password

	def retrieve_token(self,url):
		"""
		url: spotify console url where our authorization token is located
		"""

		driver = webdriver.Chrome(ChromeDriverManager().install())

		driver.get(url)

		""" 
		We our adding the function of sleep to try and imitate a person accessing the website and not a robot
		"""

		time.sleep(1)

		# close_popup= driver.find_element(By.XPATH,'//*[@id="onetrust-close-btn-container"]/button')

		# close_popup.click()

		# time.sleep(1)

		get_token = driver.find_element(By.XPATH,'//*[@id="console-form"]/div[4]/div/span/button')

		get_token.click()

		time.sleep(1)

		#playlist_modify_private is the name of the scope we are going to use on Spotify. This is where you change your scope if you decide to make you playlist public.
		playlist_modify_private = driver.find_element(By.XPATH,'//*[@id="oauth-modal"]/div/div/div[2]/form/div[1]/div/div/div[2]/div/label/span')

		playlist_modify_private.click()

		time.sleep(1)

		request_token_button = driver.find_element(By.XPATH,'//*[@id="oauthRequestToken"]')

		request_token_button.click()

		time.sleep(1)

		username_login = driver.find_element(By.XPATH,'//*[@id="login-username"]')

		username_login.send_keys(self.username)

		password_login = driver.find_element(By.XPATH,'//*[@id="login-password"]')

		password_login.send_keys(self.password)

		time.sleep(1)

		password_login.send_keys(Keys.ENTER)

		time.sleep(1)

		token = driver.find_element(By.XPATH,'//*[@id="oauth-input"]')

		self.token = token.get_attribute('value')

		driver.quit()