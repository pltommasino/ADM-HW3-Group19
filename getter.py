#Import library
from bs4 import BeautifulSoup
import time
import requests

def create_list_pagesFINDaMASTERS():
    '''
    output: list of courses pages ('pages')
    '''

    #Initialize a list
    pages = []

    #For each defined URL ('str_url') a number is added for each loop (for the first 400 pages).
    for i in range(1, 401):
        str_url = 'https://www.findamasters.com/masters-degrees/msc-degrees/?PG='
        num_pg = str(i)
        total = str_url + num_pg
        pages.append(total)

    #Return 'pages' list full
    return pages

def download_URLcourses(pages):
    '''
    in input: list of 'pages'
    output: txt file 'url-courses.txt' with all URL courses
    '''

    #Initialize a list
    courses = []

    for page in pages:

        #Requests the content of the specified web page.
        response_page = requests.get(page, timeout=10)

        #Find in all HTML page only the value of href in <a with '/masters-degrees/course'.
        for link in BeautifulSoup(response_page.content, 'html.parser').find_all('a', href=True):
            link_page = link['href']

            #If there is, clean url and append in 'courses' list
            if '/masters-degrees/course' in link_page:
                result = link_page.split('#',1)[0]
                url = 'https://www.findamasters.com' + result
                if url not in courses:
                    courses.append(url)

            #... else, continue.
            else:
                continue
        
        #Take 5 seconds off to have all links correctly
        time.sleep(5)

    #Create the file (if it does not exist) and writes for each course (in list 'courses' create before) a line in the file
    with open('url-courses.txt','w') as file:
        for course in courses:
            file.writelines(course + '\n')