
from textblob import TextBlob
import nltk
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
#open text file in read mode
text_file = open("data.txt", "r")
 
#read whole file to a string
data = text_file.read()
 
#close file
text_file.close()
 
sentiment_call = TextBlob(data)

print(sentiment_call.sentiment)


lines = data.split("\n")

impact_word = 'growth'

for line in lines:
    if impact_word in line:
        print(line)

doc = nlp(data)
print([(X.text, X.label_) for X in doc.ents])