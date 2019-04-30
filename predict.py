import External_Internal as eint
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from textpreprocessing import extract_words
ignore_words = ['http','https','www','com','xml','php','xl','asp','co','za','html','php']
def predict_key_pages(url):
    links=eint.getAllInternalLinks(url)
    ext=['.jpg','.png','.jpeg']
    clean_links=[f for f in links if f[-4:] not in ext]
    f=open('url_classify.pickle','rb')
    classifier=pickle.load(f)
    f.close()
    final_result=[]
    for link in clean_links:
        count_vectorizer = CountVectorizer(analyzer=extract_words,stop_words=ignore_words,vocabulary=['about', 'homepage',"contact",'gallery', "blog"])
        url=count_vectorizer.fit_transform([link])
        predicted_page=classifier.predict(url)[0]
        result= link + ' is predicted to be a  ' + predicted_page+ ' page'
        final_result.append(result)
    return final_result
    
#to run this
#predict_key_pages('url')
