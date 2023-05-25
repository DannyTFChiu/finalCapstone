### Compulsory Task 2 ###

import spacy
import pandas as pd

# load up the advance language module
nlp = spacy.load('en_core_web_md')

# use panda to import the text file
df = pd.read_csv('movies.txt', sep=':', header = None)

# define a function taking movie description as argument
def watch_next(description):

    movie_des = nlp(description)

    # define variable to set the initial score of recommended movie score at 0
    rec_score = 0

    # Calculate SIMILARITY Score within movie dataframe
    for i in range(len(df[0])):
        recommendation = nlp(df.iloc[i,1])
        score = recommendation.similarity(movie_des)

        if score > rec_score: # store the highest similarity score details to variables
            rec_score = score
            rec_movie = df.iloc[i,0]
            rec_movie_des = df.iloc[i,1]

    return print(f"The recommended movie to watch next is {rec_movie}, please see the description below:\n{rec_movie_des}")


# Planet Hulk - Movie Description
hulk_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator"

# Apply Planet Hulk Movie Description to the function
watch_next(hulk_description)


# LIMITATION OF FUNCTION
# What to do when there are two or more movie with same similarity score?