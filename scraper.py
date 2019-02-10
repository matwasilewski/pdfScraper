from bs4 import BeautifulSoup
import sys
import urllib.request
import re

# Get URL from console argument
url_address = sys.argv[1]

# Create request file of the webpage
webpage = urllib.request.urlopen(url_address)

# Create soup object
soup = BeautifulSoup(webpage, 'html.parser')


"""
# Downloading the HTML file of the webpage
requested_webpage = urllib.URLopener()

requested_webpage.retrieve("webpage.html", "webpage.html")


web_content = requested_webpage.read()

with open("webpage.html", mode='w') as web_file:
    web_file.write(web_content)

print(web_content[0:100])
"""
