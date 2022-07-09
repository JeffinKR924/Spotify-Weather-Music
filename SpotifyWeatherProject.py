import tkinter as tk
import requests
from PIL import Image, ImageTk
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import webbrowser


#All spotify developer credentials
cid = '39bccba7d0564635884cc8635037cb50'
secret = '67f166937a804af7bfeb494609af6c99'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Method used to open the spotify playlist in a new webpage
def callback(url):
    webbrowser.open_new(url)

#Method used to import the uri and name, and insert them in a sentence which is displayed in label
def prntspotify(x, z):
    playlistname = x
    playlisturi = z
    spotprint = ('Playlist Name: ' + str(playlistname) + '\n\n' + 'Playlist URI: ' + str(playlisturi))
    displayspotifylabel['text'] = spotprint

#Used to access the openweathermap API
def weatherreq(x):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    param = {'APPID': 'ebe3e5ec86c963f448a6c8f844916838', 'q': x, 'units': 'imperial'}
    data = requests.get(url, params=param)
    weather = data.json()
    displaylabel['text'] = finaldisplay(weather)

#Determines the weather, chooses an appropriate playlist, and stores all the information
def conditionmethod(conditionid):
    if(conditionid >= 200 and conditionid <= 232):
        i = random.randint(0,2)
        stormlist = ['3IG0HZLTspur2SvRDB2K7B', '7gA2phryO199Z4Snzw1umN', '37i9dQZF1DX2pSTOxoPbx9'] 
        x = stormlist[i]
        stormplaylist = sp.playlist(x)
        urlp = stormplaylist['external_urls']['spotify']
        namep = stormplaylist['name'] 
        urip = stormplaylist['uri']
        #Sends url and name to the method to be printed
        prntspotify(namep, urip)

        #Prints the spotify playlist url as a hyperlink
        lbl = tk.Label(displayspotifylabel, text=urlp, fg="blue", cursor="hand2")
        lbl.place(x=-3, y=70,)
        lbl.bind("<Button-1>", lambda e: callback(urlp))

    elif(conditionid >= 300 and conditionid <= 321):
        i = random.randint(0,2)
        drizzlelist = ['4vYGn4nEtwUsKmSDdoYgHm', '30ycbGQvJIvVrJ6PuXocyO', '1EFAp5brg4FmwcDvB8yA9d'] 
        x = drizzlelist[i]
        drizzleplaylist = sp.playlist(x)
        namep = drizzleplaylist['name'] 
        urlp = drizzleplaylist['external_urls']['spotify']
        urip = drizzleplaylist['uri']
        prntspotify(namep, urip)

        lbl = tk.Label(displayspotifylabel, text=urlp, fg="blue", cursor="hand2")
        lbl.place(x=-3, y=70,)
        lbl.bind("<Button-1>", lambda e: callback(urlp))

    elif(conditionid >= 500 and conditionid <= 531):
        i = random.randint(0,2)
        rainlist = ['7nMFSIFqtu4kv0SGvnJapi', '37i9dQZF1DWYxwmBaMqxsl', '4Tw7B7hezJfvCf5gyeSDoK'] 
        x = rainlist[i]
        rainplaylist = sp.playlist(x)
        namep = rainplaylist['name'] 
        urlp = rainplaylist['external_urls']['spotify']
        urip = rainplaylist['uri']
        prntspotify(namep, urip)

        lbl = tk.Label(displayspotifylabel, text=urlp, fg="blue", cursor="hand2")
        lbl.place(x=-3, y=70,)
        lbl.bind("<Button-1>", lambda e: callback(urlp))

    elif(conditionid >= 600 and conditionid <= 622):
        i = random.randint(0,2)
        snowlist = ['37i9dQZF1DWXR9b9fYSEj4', '2GQx2e99KUkPRyo9YeqWAQ', '04N8ZBCaYSJmODS9M9S2tz'] 
        x = snowlist[i]
        snowplaylist = sp.playlist(x)
        namep = snowplaylist['name'] 
        urlp = snowplaylist['external_urls']['spotify']
        urip = snowplaylist['uri']
        prntspotify(namep, urip)

        lbl = tk.Label(displayspotifylabel, text=urlp, fg="blue", cursor="hand2")
        lbl.place(x=-3, y=70,)
        lbl.bind("<Button-1>", lambda e: callback(urlp))

    elif(conditionid >= 701 and conditionid <= 781):
        i = random.randint(0,2)
        foglist = ['388VrivqLCQtmQe2ofllHc', '6Y6uugI4JJCRf0cxWuyBx2', '1bHVq4XvHZxIT18bJLgpS3'] 
        x = foglist[i]
        fogplaylist = sp.playlist(x)
        namep = fogplaylist['name'] 
        urlp = fogplaylist['external_urls']['spotify']
        urip = fogplaylist['uri']
        prntspotify(namep, urip)

        lbl = tk.Label(displayspotifylabel, text=urlp, fg="blue", cursor="hand2")
        lbl.place(x=-3, y=70,)
        lbl.bind("<Button-1>", lambda e: callback(urlp))

    elif(conditionid == 800):
        i = random.randint(0,2)
        clearlist = ['6mwwPu8x5YNABgsp0hsWq8', '2KiBoPnnKn7Q6n7rAOA6Mz', '0g0eeVagk84uHyvfCgYcuU'] 
        x = clearlist[i]
        clearplaylist = sp.playlist(x)
        namep = clearplaylist['name'] 
        urlp = clearplaylist['external_urls']['spotify']
        urip = clearplaylist['uri']
        prntspotify(namep, urip)

        lbl = tk.Label(displayspotifylabel, text=urlp, fg="blue", cursor="hand2")
        lbl.place(x=-3, y=70,)
        lbl.bind("<Button-1>", lambda e: callback(urlp))

    elif(conditionid >= 801 and conditionid <= 804):
        i = random.randint(0,2)
        cloudlist = ['0yiuaHc5LymPcvUNHj9yQG', '3So47qlswBZpIERObnkMMG', '2oWNcxKG5JyXA8DBVgNOt0'] 
        x = cloudlist[i]
        cloudplaylist = sp.playlist(x)
        namep = cloudplaylist['name'] 
        urlp = cloudplaylist['external_urls']['spotify']
        urip = cloudplaylist['uri']
        prntspotify(namep, urip)

        lbl = tk.Label(displayspotifylabel, text=urlp, fg="blue", cursor="hand2")
        lbl.place(x=-3, y=70,)
        lbl.bind("<Button-1>", lambda e: callback(urlp))

    else:
        print('Error. Please try again.')


#Stores and prints all important weather information
def finaldisplay(weather):
    location = weather['name']
    condition = weather['weather'][0]['description']
    temp = weather['main']['temp']
    tempmin = weather['main']['temp_min']
    tempmax = weather['main']['temp_max']
    feellike = weather['main']['feels_like']
    humid = weather['main']['humidity']
    windspeed = weather['wind']['speed']
    conditionid = weather['weather'][0]['id']
    finalprnt = ('Location: ' + location + '\n\n' + 'Condition: ' + condition + '\n\n' + 'Temperature: ' + str(temp) + 'ºF' + '\n\n' + 'Minimum Temp: ' + str(tempmin) + 'ºF' + '\n\n' + 'Maximum Temp: ' + str(tempmax) + 'ºF' + '\n\n' + 'Feels Like: ' + str(feellike) + 'ºF' + '\n\n' + 'Humidity: ' + str(humid) + '%'+ '\n\n' + 'Wind Speed: ' + str(windspeed) + 'mph') 
    conditionmethod(conditionid)
    return finalprnt


board = tk.Tk()

#Creates the window
canvas = tk.Canvas(board, height = 600, width = 800)
canvas.pack()

#Resizes the window
board.geometry('850x620')
board.resizable(width=0, height=0)

#Imports a background image and creates a label to display it
image = Image.open(r"C:Extra Stuff\pic1.jpg")
image = image.resize((850, 620), resample=Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label = tk.Label (image=photo)
label.image = photo 
label.place(x=0, y=0, relwidth=1, relheight=1)

#Creates frame for the search bar
frame = tk.Frame(board, bg='#1DB954', bd=3)
frame.place(relx=0.5, rely=0.1, relwidth=0.65, relheight=0.06, anchor='n')

#Creates the entry for the search bar
entry = tk.Entry(frame, font=40, relief='flat')
entry.place(relwidth=0.65, relheight=1)

#Creates the button for the search bar
button = tk.Button(frame, text="Enter", bg='#000000', fg='#FFFFFF', activebackground='#1DB954', relief='raised', command=lambda: weatherreq(entry.get()), )
button.place(relx=0.65, relheight=1, relwidth=0.3)

#Creates a frame for the weather info display
displayframe = tk.Frame(board, bg='#1DB954', bd=3)
displayframe.place(relx=0, rely=0.25, relwidth=0.475, relheight=0.7)

#Creates a label for the weather info display
displaylabel = tk.Label(displayframe, anchor = 'nw', justify='left')
displaylabel.place(relx=0.02375, rely=0.03, relwidth=0.95, relheight=0.95)

#Creates a frame for the spotify info display
displayspotifyframe = tk.Frame(board, bg='#1DB954', bd=3)
displayspotifyframe.place(relx=0.5248, rely=0.25, relwidth=0.475, relheight=0.7)

#Creates a label for the spotify info display
displayspotifylabel = tk.Label(displayspotifyframe, anchor = 'nw', justify='left')
displayspotifylabel.place(relx=0.024, rely=0.03, relwidth=0.95, relheight=0.95)

#Runs the program
board.mainloop()