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
#In order to test script:Use code below

# getAllExternalLinks('https://theblowfishgroup.com/hotel/')
#getAllInternalLinks('https://theblowfishgroup.com/hotel/')

