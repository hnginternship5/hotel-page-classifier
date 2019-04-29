from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
#dependancies
from sumy.summarizers.lex_rank import LexRankSummarizer 
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
import re
import datetime
import random
import pandas as pd
import numpy as np
import urllib
from collections import OrderedDict
import warnings
warnings.filterwarnings("ignore")
import sys, os
import argparse


summarizer = LexRankSummarizer()
pages = set() 
random.seed(datetime.datetime.now())

def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme,urlparse(includeUrl).netloc)    
    internalLinks = []    #Finds all links that begin with a "/"
    for link in bs.find_all('a',href=re.compile('^(/|.*'+includeUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl+link.attrs['href'])                
                else:      
                    internalLinks.append(link.attrs['href'])
    return internalLinks


def getExternalLinks(bs,excludeUrl):
    externalLinks =[]
  
    for link in bs.find_all('a',href=re.compile('^(https|http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


#-------------------------------------------------------------------------------------------------#
# Collects a list of all external URLs found on the site
allExtLinks = set() 
def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    domain = '{}://{}'.format(urlparse(siteUrl).scheme,urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, domain)
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks(link)

#------------------------------------------------------------------------------------------------#
# Collects a list of all internal URLs found on the site

allIntLinks = set()
def getAllInternalLinks(siteUrl):
    html = urlopen(siteUrl)
    domain = '{}://{}'.format(urlparse(siteUrl).scheme,urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)
  
    for link in internalLinks:
        if link not in allExtLinks:
            allIntLinks.add(link)
            print(link)
      

#-----------------------------------------------------------------------------------------------#
#In order to test script:Use code below

#getAllExternalLinks('https://theblowfishgroup.com/hotel/')
#getAllInternalLinks('https://theblowfishgroup.com/hotel/')

#containers to append text extracted from tags & links
scrapped_link = []
scrapped_contact = []


#internal Links getter
def url(siteUrl):
    html = urlopen(siteUrl)
    domain = '{}://{}'.format(urlparse(siteUrl).scheme,urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)    
    return internalLinks

#parser for link tags
def parser(link):
    response = urlopen(link)
    html = response.read()
    parsed_html = BeautifulSoup(html, 'html.parser')
    return parsed_html


#get text from tags in each internal link and save into a dataframe 
def CreateDataSet(w):
    try:
        urls = url(w) 
        for link in urls:
            if link not in allExtLinks:
                find_about = link
                # Create a list of each bit between slashes
                slashparts = find_about.split('/')
                dirname = '/'.join(slashparts[:-1]) + '/'
                if ("contact-us" or "contact" or "contact us") in slashparts:
                    scrapped_contact.append(link)
                    print('\n',link)

                    for contact in  scrapped_contact:   
                        parser = HtmlParser.from_url(link, Tokenizer("english"))
                        summary = summarizer(parser.document, 2)
        #                 print(l, '\n')
                        #saving the summary to a dataframe
                        for sentence in summary:        
                            print(sentence, '\n')
                        break 
        else:
            if len(scrapped_contact) > 0:
                quit()
            print('There is no "contact-us" linked pages in this url')
    except:
        print('There seem to be an issue with the Url you entered')
        quit()
            
            
        
def main():
    parser = argparse.ArgumentParser()        
 #   parser.add_argument('action',help='this would search "abouts" in the inner links of the url')
    parser.add_argument("web", help='add a url to the about.py command', type=str )
    args = parser.parse_args()
    result = CreateDataSet(args.web)
if __name__=='__main__':
    main()
