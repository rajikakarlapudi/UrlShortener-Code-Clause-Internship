# Pyshorteners is a Python module that provides 
# implementation for various URL Shortening services 
#that are available in the market. 

import pyshorteners
url=input("Enter the long_url to get shortened: ")

def shorten_url(url):
    #Shortener() function condenses the url
    s=pyshorteners.Shortener()
    #tinyurl method accepts the long url as parameter and shortens it.
    print("The shortened Url is :")
    print(s.tinyurl.short(url))

shorten_url(url)