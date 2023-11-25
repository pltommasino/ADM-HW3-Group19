# Homework 3 - Master's Degrees from all over!
## ADM - Group 19
### Introduction

This project was carried out by Group 19 of Algorithmic Methods for Data Mining, consisting of:

| NAME and SURNAME | EMAIL |
| --- | --- |
| Pasquale Luca Tommasino | tommasino.1912107@studenti.uniroma1.it | 
| Elias Antoun | antoun.2128572@studenti.uniroma1.it |
| Jacopo Orsini | orsini.2099929@studenti.unirom1.it |
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
0. Preprocessing:
0.0. Preprocessing: Defined a fucntion to tokenize, remove stopwords and punctuation and lemmatize the description column.
0.1. Fee Standardization: Get currency conversion rates(updated daily) from currency_converter, and detect amounts and currencies from the fees column and convert according to country or currency detected. Note that in this part I tried using forex but it was extremely slow.
   
2. Conjunctive query: the goal of this task is to create a function that takes as input a word (or more words) from the "description" attribute of the dataset, extracted in the point 1 and cleaned in the preprocessing phase, and returns all the documents that have that word in the description field, in particular it gives back 4 columns ("courseName", "universityName", "description" and "url") where eache row represents a document. The implementation of this query was possible thanks to the creation of a vocabulary, that asscoiates a word with an id and after of a file id, and a file which associates to each term a series of documents in which that term is present.

3. Conjunctive query and ranking score: this query represents an evolution of the previous one adding the "similarity" as a new paramenter for the generation of the output. In our case, are printed the top k (with k=10) courses that have the highiest similarity with the query input. This new parameter has been created by implementing the cosine_similarity function, just after the generation of a new invertex index using the tifidf.

   

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
In this part, we firtly used opensource geocoding api 'Geocoder'. By giving college names to API, we get latitude and longitude values for every college and added these values to ranked master degree dataframe. (You can see the last version of the data in the master_ranked_lat_lot.csv). After that, by using folium map library, we put these information on the map with the cost information and save this map as .html file. (university_map.html).

### 5. BONUS: More complex search engine


### 6. Command Line Question - UMUT

In this section, we merged .tsv files with command line commands as merged_courses.tsv.  After that we did some data exploration as question suggest and print those results on the terminal screen. We saved all these commands into CommandLine.sh file.

### 7. Algorithmic Question - PASQUALE and JACOPO

Preliminary assumption:
   - We assume that Leonardo can have 0 hours of work in a day, so cases in which 0 is chosen among the range of hours are allowed
   - We assume that the largest range of hours can be [0,8], so a day of work can't have more than 8 hours (even without this constratin the algorithm would work as well)

1. The aim of this question is to perfrom an algorithm that is able to calculate, starting from 3 inputs:
   - d: the number of days of work;
   - sumHours: the number of hours of work, in the d days;
   - ranges: the d intervals (one for each day of work) with a min of hours of work to a max of hours of work;
   That is able to calculate a combination of hours worked per each day respecting the input data.
   
   The idea behind it is the following one:
   - Given the 3 inputs, the machine calculates all the possible combinations of hours worked each day;
   - After calcuating all the combinations, all those for which the sum of hours worked for the single range is different from the sum of hours worked are discarded, an example: given d=3, sumHours=5 and ranges: d1
     [0,1], [0,2], [1,3], the computer will calculate all the possible combinations of hours of work, for example a combination can be d1=1, d2=1 and d3=3, in this case as long as the sum of these 3 element is exactly 
     equal to sumHours, this combination will be kept; an alternavtive combination could have been: d1=1, d2=1 and d3=2, the sum is different from 5 and this combination will be discared;
   - If there is a solution "YES" is printed together with the number of hours per each day (if there is more than 1 solution, just a random one is printed among all the right combinations), if there isn't a solution 
     just "NO" is printed.

2. The 'time complexity' (Big O notation) for our algorithm is $O(n^2)$. This is because the Big O notation goes to analyze the worst case of the algorithm. In our case, the worst case is when the algorithm needs to calculate all possible combinations for our exercise. All the details on the calculation are provided in the main file of this repository.

3. The answer given by ChatGPT on the calculation of the Big O notation corresponds to the one we did.

4. We believe that our code is mostly functional according the way we solved it (exlaination in point 1); probably a more optimal solution to this problem does exist, but assuming that we change the structure behind the code itself.
