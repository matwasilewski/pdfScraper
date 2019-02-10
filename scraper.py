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

filename_regex = re.compile('(\w*.pdf)$')

# Find every tag 'a' in the soup
for link in soup.findAll('a', attrs={'href': re.compile("^http://.*(/\w*\.[pP][dD][fF])$")}):
    
    # save direct link to the pdf as a separate variable
    link_pdf = link.get('href')

    # uncomment for testing purposes
    # print(link_pdf)
    
    match_object = filename_regex.search(link_pdf)
    #match_object = re.match(filename_regex, link_pdf)
    filename = match_object.group(0)
    
    try: 
        urllib.request.urlretrieve(link_pdf, filename) 
    
    except urllib.error.HTTPError as e:
        print("Sorry, there is nothing at this link! Proceeding to the next!")
