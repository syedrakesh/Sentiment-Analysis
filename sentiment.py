from textblob import TextBlob
import nltk
from newspaper import Article

print('Enter sentence: ')
input = input()

obj = TextBlob(input)
sentiment = obj.sentiment.polarity

if sentiment == 0:
    print('The sentence is neutral.')
	
elif sentiment > 0:
    print('The sentence is positive.')
	
else:
    print('The sentence is negative')