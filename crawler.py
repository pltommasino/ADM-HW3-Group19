#Import library
import os.path
import time
import requests

def download_courses(txt, counter_page):
    '''
    in input:=  'txt': a .txt file 'courses' (by default is 'url-courses.txt')
                'counter_page': page number where to start the download
                
    output:= download .html files courses, divided for page (in path)
    '''

    #Initialize one counter for 'course' in a page and another for 'page'
    counter_course = 1

    with open(txt,'r') as file:
        #For each course in file 'url-courses.txt'...
        courses_lines = file.readlines()
        file.close()

    for course in courses_lines:

        #Create a right folder for each course
        path = 'html_page' + str(counter_page) + '/'

        course = course.strip()
        #Requests the content of the specified web page.
        response_course = requests.get(course, timeout=100)
        time.sleep(5)
        path_in1 = 'page' + str(counter_page) + '_course' + str(counter_course) + '.html'
        path_in = path + path_in1

        #If path doesn't exist, make directory
        pathcomplete = 'html/' + path
        if not os.path.exists(pathcomplete):
            os.makedirs(pathcomplete)

        #If file already exist pass, otherwise codelines above creates and write in it
        try:
            with open('html/' + path_in,'r') as f:
                print('Found HTML file for the Course nr. %s on Page nr. %s' %(counter_course, counter_page))
                pass
        except FileNotFoundError:
            with open('html/' + path_in, 'wb+') as file2:
                file2.write(response_course.content)
                print('*Created* HTML file for the Course nr. %s on Page nr. %s' %(counter_course, counter_page))
                time.sleep(5)

        counter_course += 1
    
        if counter_course == 16:
            print('Downloading done for the courses in page nr. %i' %counter_page)
            counter_page += 1
            counter_course = 1


def check_file_exist():
    '''
    output:= 'npage': first page number that does not have the download
    '''
    #Initialize a 'number of break cycle for' in 0. It means not break the cycle. If it is 1 break all cycle.
    nbr = 0

    #Search in each course in each page...
    for npage in range(1,401):
        if nbr == 1:
            break
        for ncourse in range(1,16):
            path = 'html/html_page' + str(npage) + '/page' + str(npage) + '_course' + str(ncourse) + '.html'
            
            #If the path not exist, it broke all cycle for
            if not os.path.exists(path):
                print('The file at the following path could not be found: ' + path + '. The courses in this page will be verified again.')
                nbr = 1
                return npage