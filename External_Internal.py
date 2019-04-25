# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 12:31:45 2019

@author: Jesse Amamgbu
"""
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random


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
#Note that runung the code above is a requisite for runing the following codes below 
#and specially written with respect to the valid_website.csv dataframe on the repo 
#-----------------------------------------------------------------------------------------------#
#containers to append text extracted from tags & links
scrapped_link = []
scrapped_tiles = []
scrapped_h1 = []
scrapped_h2 = []
#-----------------------------------------------------------------------------------------------#
#internal Links getter
def url(siteUrl):
    html = urlopen(siteUrl)
    domain = '{}://{}'.format(urlparse(siteUrl).scheme,urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)    
    return internalLinks
#-----------------------------------------------------------------------------------------------#
#parser for link tags
def parser(link):
    response = urlopen(link)
    html = response.read()
    parsed_html = BeautifulSoup(html, 'html.parser')
    return parsed_html
#-----------------------------------------------------------------------------------------------#
#get text from tags in each internal link and save into a dataframe 
def CreateDataSet(df):
    for siteUrl in df.valid_website:
        try:
            urls = url(siteUrl) 
        except:
#             print('loading error')
            pass         
        for link in urls:
            try:
                parse = parser(link)
                try:
                    titles = parse.head.find('title').text
                except: 
#                     print('couldnt get title')
                    pass
                try:
                    h1 = parse.html.find('h1').text
                except:
#                     print('couldnt get h1 tag')
                    pass
                try:
                    h2 = parse.html.find('h2').text
                except:
#                     print('couldnt get h2 tag')
                    pass
            except:
                pass
            
            if link not in allExtLinks:
                allIntLinks.add(link)    
                scrapped_link.append(link)
                scrapped_tiles.append(titles)
                scrapped_h1.append(h1)
                scrapped_h2.append(h2)
                
    data = pd.DataFrame(OrderedDict({'links':scrapped_link,
                                     'title':scrapped_tiles,
                                     'h1':scrapped_h1,
                                     'h2':scrapped_h2}))
    data.to_csv('hotel-page-classifier_dataset.csv',
                encoding='utf-8', 
                index=False)  
    print('hotel-page-classifier_dataset.csv is saved to your PC')
    display(data.head())
#-----------------------------------------------------------------------------------------------#
#In order to test script:Use code below

# getAllExternalLinks('https://theblowfishgroup.com/hotel/')
#getAllInternalLinks('https://theblowfishgroup.com/hotel/')
#CreateDataSet(dataframe)
