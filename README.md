
# Spotify-Weather Music

This program allows the user to look up the current weather of any location, and also be recommended a Spotify playlist based on the weather of that location. 

You will receive the following information for any location that is entered:

**Weather Information:**\
Location\
Condition\
Temperature(°F)\
Minimum Temp(°F)\
Maximum Temp(°F)\
Feels Like(°F)\
Humidity(%)\
Wind Speed(mph)

**Spotify Information:**\
Playlist Name\
Playlist URI\
PLaylist HyperLink





## Usage
Run the Python file to open up the program interface. Type in a location in the search bar and press the search button to retrieve the information. To access the Spotify playlist, you can use the URI, or press on the hyperlink to automatically take you to the playlist through your webbrowser.

**NOTE:** Pressing the ENTER key on your keyboard won't initiate a search\
**NOTE:** If the information does not show up after you search for the location, then either there is a typo with what was entered, or that location is not supported with the weather API


## API Reference

#### Weather API
\
**Can access API from: [openweathermap.org](https://openweathermap.org/)**

```
  requests.get(url, params)
```

| URL       | Type     | Description                                               |
| :-------- | :------- | :---------------------------------------------------------|
| `url`     | `string` | **Required**. URL of the weather api with desired version |


| Params | Type     | Description                             |
| :-------- | :------- | :------------------------------------|
| `API key` | `string` | **Required**. Your key to access API |



#### Spotify API
\
**Can access API from: [developer.spotify.com](https://developer.spotify.com/)**

```
  SpotifyClientCredentials(client_id, client_secret)
```

| client_id | Type     | Description                                               |
| :-------- | :------- | :---------------------------------------------------------|
| `API key` | `string` | **Required**. Your personal API key to access Spotify API |

| client_secret | Type     | Description                                                                              |
| :--------     | :------- | :---------------------------------------------------------                               |
| `project code`| `string` | **Required**. The project code given after creating project in developer spotify account |

**NOTE:** A python library for the spotify Web API is required. **SpotiPy** is recommended \
**(Docs for SpotiPy: [spotipy.readthedocs.io](https://spotipy.readthedocs.io/en/master/))**






## Acknowledgements

 - Spotify Information and built in Methods Imported from [developer.spotify.com](https://developer.spotify.com/)
 - Weather Information and built in Methods Imported from [openweathermap.org](https://openweathermap.org/)
 - SpotiPY built in Methods Created with help from [spotipy.readthedocs.io](https://spotipy.readthedocs.io/en/master/)
 - Tkinter built in Methods Imported from [tutorialspoint.com](https://tutorialspoint.dev/language/python/python-gui-tkinter)
 - Weather Functionality and Tkinter Integration Created with help from Youtuber: [Keith Galli](https://www.youtube.com/c/KGMIT/featured)
 

## 🚀 About the Creator
My name is Jeffin Rajan and I am a Computer Science major at Drexel University. I created this program by myself in my Senior year of HighSchool. **This program was created and submitted for the 2020 AP Computer Science Principles Exam**


## 🔗 Links
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](http://www.github.com/JeffinKR924)
[![Stack Overflow](https://img.shields.io/badge/-Stackoverflow-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white)](https://www.stackoverflow.com/users/19504427/jeffin-rajan)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jeffin-k-rajan/)
[![Discord](https://img.shields.io/badge/discord-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discordapp.com/users/750429356739788933/)


