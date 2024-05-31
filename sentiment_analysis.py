# In this project we read an Amazon customer reviews comma seperated values file
# and try and analyze the sentiment of the customer reviews based on the colunm reviews.text
# which contains the customers reviews.
# We use pandas to read the file and use spaCy to tokenize the words so we can apply our
# sentiment analysis on the words.
# Finally we use TextBlob in textblob to perform a sentiment analysis on the responses to
# determine the positive responses, the negative responses and the neutral responses.

# Two functions are used in the project.  The firs being def preprocess() which is usd to preprocess the data
# and returns lemmatized phrases. The second function used is the def analyze_polarity which is used
# for the sentiment analysis on the phrases in the series.

import numpy as np
import pandas as pd
import spacy
from textblob import TextBlob

nlp = spacy.load('en_core_web_sm')


# The function below extracts lemmatized words without stopwords and punctuations
def preprocess(cleaned_data):
    doc = nlp(cleaned_data.lower().strip())
    processed = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    #print(processed)

    return ' '.join(processed)  #This joins the processed words into sentences using whitespaces

def analyze_polarity(cleaned_data):
    # Preprocess the text with spaCy
    doc = nlp(cleaned_data)

    # Analyze sentiment with TextBlob
    blob = TextBlob(cleaned_data)
    polarity = blob.sentiment.polarity

    return polarity


# read the CSV file using pandas and store in the dataframe named amazon
amazon = pd.read_csv('amazon_product_reviews.csv')  

# Move the dataframe amazon into reviews_data series
reviews_data = amazon[['reviews.text']]

# You can check for and remove blank rows using the dropna function below
# Use the below to remove any missing values from the columns
reviews_data = reviews_data.dropna(subset=['reviews.text'])
print(reviews_data.isnull().sum()) # check that there are no null values to clean
# reviews_data.dropna(inplace=True, axis=0) # to drop them
# You can use the .isnull.sum() to check for null values and sum them up


cleaned_data = reviews_data['reviews.text']
# print(cleaned_data)

# The line below is used to call the function and apply it to each item in the series (a series is a one-dimensional dataframe)
reviews_data['processed.text'] = cleaned_data.apply(preprocess)

#  We extract the values stored in the dataframe into the variable named 'data' using the .values attribute
data = reviews_data['processed.text'].values

sentiments = []

for item in data:
    #print(item)
    polarity_score = analyze_polarity(item)

    if polarity_score > 0:
        sentiment = "positive"
    elif polarity_score < 0:
        sentiment =  "negative"
    else:
        sentiment = "neutral"

    sentiments.append(sentiment)

print(sentiments)

positive_responses = sentiments.count("positive")
negative_responses = sentiments.count("negative")
neutral_responses = sentiments.count("neutral")

total_responses = len(sentiments)

positive_percentage = positive_responses/total_responses * 100
negative_percentage = negative_responses/total_responses * 100
neutral_percentage = neutral_responses/total_responses * 100

print(f"Percentage of positive responses: {positive_percentage:.2f}%")
print(f"Percentage of negative responses: {negative_percentage:.2f}%")
print(f"Percentage of neutral responses: {neutral_percentage:.2f}%")
