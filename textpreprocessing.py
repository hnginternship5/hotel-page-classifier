import pandas as pd
df=pd.read_csv('FinalCsv.csv', names=['Url','label'])
print(df.head())

import re
ignore_words = ['http','https','www','com','xml','php','xl','asp','co','za','html','php']
def extract_words(sentence):
    words = re.sub("[^\w]", " ",  sentence).split() #nltk.word_tokenize(sentence)
    words_cleaned = [w.lower() for w in words if w not in ignore_words]
    return words_cleaned
df['Tokens'] = df['Url'].apply(lambda x: extract_words(x))

print(df.head())