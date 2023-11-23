# Homework 3 - Master's Degrees from all over!
## ADM - Group 19
### Introduction

This project was carried out by Group 19 of Algorithmic Methods for Data Mining, consisting of:

| NAME and SURNAME | EMAIL |
| --- | --- |
| Pasquale Luca Tommasino | tommasino.1912107@studenti.uniroma1.it | 
| Elias Antoun | - | antoun.2128572@studenti.uniroma1.it
| Jacopo Orsini | - |
| Umut | - |


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


### 1. Data Collection - PASQUALE

We built our dataset through several steps, and for each step, a dedicated file was created in Python:

1. Get the list of master's degree courses:
> The purpose of this section is to want to collect the URL associated with each site. For this, we created __`getter.py`__. This Python script create the file `url-courses.txt` whose single line corresponds to the master's URL.

2. Crawl master's degree pages:
> The purpose of this section is to want to do the HTML download of each URL listed before. For this, we created __`crawler.py`__. This Python script create, for each course, an `.html` file, and put it in a specific path in `\html` folder.

3. Parse downloaded pages:
> The purpose of this section is to want to read each previously downloaded HTML file, and take the information we need to build the dataset. For this reason we create __`parser.py`__ Python script. For each master's degree, we create a `.tsv` file and only after that, putting these files together, we created the dataset `dataset_courses.csv`

In addition, an extra file __`functioner.py`__ was created. Within it are defined all the functions that were needed for the proper functioning of the files listed earlier


### 2. Search Engine - JACOPO and ELIAS
0. Preprocessing: ELIAS
0.0. Preprocessing: Defined a fucntion to tokenize, remove stopwords and punctuation and lemmatize the description column.
0.1. Fee Standardization: Get currency conversion rates(updated daily) from currency_converter, and detect amounts and currencies from the fees column and convert according to country or currency detected. Note that in this part I tried using forex but it was extremely slow.

   

### 3. Define a new score! - ELIAS
In this part we worked to define a new more comprehensive scoring function and return the top k matches from the dataset.
The scores are broken down as follows:
1- description score similar to what was done in 2.1
2- exact title match score
3- location score check if the user inputs a specific city/country in the query
4- fee score: check whether university is within budget
5- administration score (online or on campus)
Finally the returned score takes into account all of the functions defined above, assigning weights to each score depending on its importance(description>title>...)

### 4. Visualizing the most relevant MSc degrees - UMUT


### 5. BONUS: More complex search engine


### 6. Command Line Question - UMUT


### 7. Algorithmic Question - PASQUALE and JACOPO
