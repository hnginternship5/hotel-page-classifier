import argparse
import sys
from External_Internal import getAllInternalLinks as gAI
from textpreprocessing import *

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-u',
        '--url',
        help='This should be the url of the web page to be processed'
    )
    
    if parser.parse_args().url is None:
    	parser.error("You need to pass in a value for --url")
    return parser.parse_args()

if __name__ == "__main__":
	args = parse_args()
	url = args.url

	def predictor(url):
	  scraped_url = gAI(url)
	  for link in scraped_url:
	  	#dt is a variable from the textpreprocessing module
	    y_pred= dt.predict(count_vectorizer.fit_transform([link]))
	    print(y_pred, link)
	    
	predictor(url)