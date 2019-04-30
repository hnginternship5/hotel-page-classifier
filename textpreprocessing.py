import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
df=pd.read_csv('FinalCsv.csv', names=['Url','label'])
#print(df.head())

import re
ignore_words = ['http','https','www','com','xml','php','xl','asp','co','za','html','php']
def extract_words(sentence):
    words = re.sub("[^\w]", " ",  sentence).split() #nltk.word_tokenize(sentence)
    words_cleaned = [w.lower() for w in words if w not in ignore_words]
    return words_cleaned
df['Tokens'] = df['Url'].apply(lambda x: extract_words(x))

#print(df.head())

def list_to_str(x):
    new_x=''
    for i in x:
        new_x+= ' '+i
    return new_x

df['Tokens']=df['Tokens'].apply(list_to_str)
le= LabelEncoder()
df['label']=le.fit_transform(df['label'])

x=df['Tokens']
y=df['label']

vectorizer =TfidfVectorizer(decode_error='ignore')
x=vectorizer.fit_transform(x)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)



