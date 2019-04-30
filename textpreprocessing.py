import pandas as pd
df=pd.read_csv('FinalCsv.csv', names=['Url','label'])

import re
ignore_words = ['http','https','www','com','xml','php','xl','asp','co','za','html','php']
def extract_words(sentence):
    words = re.sub("[^\w]", " ",  sentence).split() #nltk.word_tokenize(sentence)
    words_cleaned = [w.lower() for w in words if w not in ignore_words]
    return words_cleaned
df['Tokens'] = df['Url'].apply(lambda x: extract_words(x))


import re
ignore_words = ['http','https','www','com','xml','php','xl','asp','co','za','html','php']
def extract_words(sentence):
    words = re.sub("[^\w]", " ",  sentence).split() #nltk.word_tokenize(sentence)
    words_cleaned = [w.lower() for w in words if w not in ignore_words]
    return words_cleaned
df['Tokens'] = df['Url'].apply(lambda x: extract_words(x))
from sklearn.model_selection import train_test_split
x= df['Url']
y=df['label']
from sklearn.feature_extraction.text import CountVectorizer

count_vectorizer = CountVectorizer(analyzer=extract_words,stop_words=ignore_words,vocabulary=['about',"contact",'gallery', "blog"])
count_train = count_vectorizer.fit_transform(x)
feature_names = count_vectorizer.get_feature_names()
X_vect = pd.DataFrame(count_train.toarray())
from sklearn.tree import DecisionTreeClassifier
dt= DecisionTreeClassifier()
dt.fit(X_vect,y)