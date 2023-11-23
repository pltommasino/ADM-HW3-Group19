# Homework 3 - Master's Degrees from all over!
## ADM - Group 19
### Introduction

This project was carried out by Group 19 of Algorithmic Methods for Data Mining, consisting of:

| Name and Surname | Email |
| Pasquale Luca Tommasino | tommasino.1912107@studenti.uniroma1.it | 
| Elias Antoun | |
| Jacopo Orsini | |
| Umut | |


### Description of the project

For this homework, there is no provided dataset. We have to build our own. *Description_________* 

The project is divided in this points:
1. Data Collection
2. Search Engine
3. Define a new score!
4. Visualizing the most relevant MSc degrees
5. BONUS: More complex search engine
6. Command Line Question
7. Algorithmic Question


### 1. Data Collection

We built our dataset through several steps, and for each step, a dedicated file was created in Python:

1. Get the list of master's degree courses:
> The purpose of this section is to want to collect the URL associated with each site. For this, we created __`getter.py`__. This Python script create the file `url-courses.txt` whose single line corresponds to the master's URL.

2. Crawl master's degree pages:
> The purpose of this section is to want to do the HTML download of each URL listed before. For this, we created __`crawler.py`__. This Python script create, for each course, an `.html` file, and put it in a specific path in `\html` folder.

3. Parse downloaded pages:
> The purpose of this section is to want to read each previously downloaded HTML file, and take the information we need to build the dataset. For this reason we create __`parser.py`__ Python script. For each master's degree, we create a `.tsv` file and only after that, putting these files together, we created the dataset `dataset_courses.csv`

In addition, an extra file __`functioner.py`__ was created. Within it are defined all the functions that were needed for the proper functioning of the files listed earlier


### 2. Search Engine


### 3. Define a new score!


### 4. Visualizing the most relevant MSc degrees


### 5. BONUS: More complex search engine


### 6. Command Line Question


### 7. Algorithmic Question
