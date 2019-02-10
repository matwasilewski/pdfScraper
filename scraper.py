from bs4 import BeautifulSoup
import sys
import urllib.request
import re
import os

# Get URL from console argument
url_address = sys.argv[1]

# Get directory path from console argument
directory_path = sys.argv[2]

# Create request file of the webpage
webpage = urllib.request.urlopen(url_address)

# Create soup object
soup = BeautifulSoup(webpage, 'html.parser')

# define regex to name each particular PDF.
filename_regex = re.compile('(\w*)/(\w*.pdf)$')

# Find every tag 'a' in the soup
for link in soup.findAll('a', attrs={'href': re.compile("^http://.*(/\w*\.[pP][dD][fF])$")}):
    
    # save direct link to the pdf as a separate variable
    link_pdf = link.get('href')

    # uncomment for testing purposes
    # print(link_pdf)
   
    # Create match object
    match_object = filename_regex.search(link_pdf)
    
    # Print matches - uncomment for testing purposes
    # print(match_object.groups())

    # Get filename and directory_name 
    directory_name = directory_path + match_object.group(1) 
    filename = directory_name + '/' + match_object.group(2)
    
    # uncomment for testing purposes
    # print("Directory: " + directory_name)
    # print("Filename: " + filename)

    # Create directory
    try:
        # Create target Directory
        os.mkdir(directory_name)
    except FileExistsError:
        pass

    # Download PDFs
    try:
        # print(filename)
        urllib.request.urlretrieve(link_pdf, filename) 
    
    except urllib.error.HTTPError as e:
        print("Sorry, there is nothing at this link! Proceeding to the next one!")
