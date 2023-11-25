#Import library
from bs4 import BeautifulSoup
import os.path
import pandas as pd
import csv

def download_tsv():
    '''
    output:= download .tsv files courses
    '''

    for npag in range(1,401):
        for ncour in range(1,16):
            n_course = 'page' + str(npag) + '_course' + str(ncour)
            path = 'html/html_page' + str(npag) + '/' + n_course + '.html'

            with open(path, 'r') as file: 
                        
                beautifulSoupText = BeautifulSoup(file.read(), 'html.parser') 

                #1. courseName
                try:
                    courseName = beautifulSoupText.find('h1', class_='text-white course-header__course-title').text
                    courseName = courseName.translate({ord('\xa0'): None})
                except AttributeError:
                    courseName=''

                #2. universityName
                try:
                    universityName = beautifulSoupText.find('a', class_='course-header__institution').text
                except AttributeError:
                    universityName = ''


                #3. facultyName
                try: 
                    facultyName = beautifulSoupText.find('a', class_='course-header__department').text
                except AttributeError:
                    facultyName = ''


                #4. isItFullTime
                try:
                    isItFullTime = beautifulSoupText.find('a', class_='inheritFont concealLink text-decoration-none text-gray-600').text
                except AttributeError:
                    isItFullTime = ''


                #5. description
                try:
                    description = beautifulSoupText.find('div', class_='course-sections__content').text
                    description = description.translate({ord('\n'): None})
                except AttributeError:
                    description = ''


                #6. startDate
                try:
                    startDate = beautifulSoupText.find('span', class_='key-info__content key-info__start-date py-2 pr-md-3 text-nowrap d-block d-md-inline-block').text
                except AttributeError:
                    startDate = ''


                #7. fees
                try:
                    list_fees_qq = []
                    for tag in beautifulSoupText.find_all('div', class_='course-sections__content'):
                        list_fees_qq.append(tag)
                    try:
                        select = (list_fees_qq[2].p).text
                        fees = select
                    except AttributeError:
                        select = (list_fees_qq[3].p).text
                        fees = select
                except IndexError:
                    fees = ''

                #8. modality 
                try:
                    modality = beautifulSoupText.find('a', class_='inheritFont concealLink text-gray-600 text-decoration-none').text
                except AttributeError:
                    modality=''

                
                #9. duration
                try:
                    duration = beautifulSoupText.find('span', class_='key-info__content key-info__duration py-2 pr-md-3 d-block d-md-inline-block').text
                except AttributeError:
                    duration=''


                #10. city
                try:
                    city = beautifulSoupText.find('a', class_='card-badge text-wrap text-left badge badge-gray-200 p-2 m-1 font-weight-light course-data course-data__city').text
                except AttributeError:
                    city = ''


                #11. country
                try:
                    country = beautifulSoupText.find('a', class_='card-badge text-wrap text-left badge badge-gray-200 p-2 m-1 font-weight-light course-data course-data__country').text
                except AttributeError:
                    country = ''


                #12. administration
                try: 
                    administration = beautifulSoupText.find('a', class_='card-badge text-wrap text-left badge badge-gray-200 p-2 m-1 font-weight-light course-data course-data__on-campus').text 
                except AttributeError:
                    try:
                        administration = beautifulSoupText.find('a', class_='card-badge text-wrap text-left badge badge-gray-200 p-2 m-1 font-weight-light course-data course-data__online').text
                    except AttributeError:
                        administration = ''


                #13. url
                try:
                    url_page = beautifulSoupText.find('link', href=True)
                    url = url_page['href']
                except AttributeError:
                    url = ''

                
                #Put all the value in a list
                course = [courseName, universityName, facultyName, isItFullTime, description, startDate, fees, modality, duration, city, country, administration, url]

                #Create a path to put the files .tsv ('tsv/')
                path_in = 'tsv/'

                #If the path not exists, the lines create it
                if not os.path.exists(path_in):
                    os.makedirs(path_in)

                #Create the file '.tsv' and write in it
                if not os.path.exists(path_in + n_course + '.tsv'):
                    with open(path_in + n_course + '.tsv', 'w', encoding='utf-8') as file:
                        file.write('\t'.join(course))
                else:
                    print('The file ' + n_course + '.tsv has already been created')
                    continue

def download_dataset_csv(file_name):
    '''
    input:= 'file_name': file name of dataset (include also '.csv')
    output:= download .csv dataset of courses
    '''

    cols = ['courseName','universityName','facultyName','isItFullTime','description','startDate','fees','modality','duration','city','country','administration','url']

    file_list = []

    for npage in range(1,401):
        for ncourse in range(1,16):
            path = 'tsv/page' + str(npage) + '_course' + str(ncourse) + '.tsv'

            df1 = pd.read_csv(path, header=None, names=cols, delimiter='\t', quoting=csv.QUOTE_NONE)

            file_list.append(df1)
        
    df = pd.concat([file for file in file_list], ignore_index=True)

    # Salva il dataframe in formato csv
    df.to_csv(file_name)