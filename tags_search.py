import External_Internal
from bs4 import BeautifulSoup as bs
import requests

def fetch_page(siteUrl):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	page_object = requests.get(siteUrl, headers=headers)
	page_content = page_object.content
	return page_content

def find_title_tags(page_content):
	bs_content = bs(page_content, "html.parser")
	return bs_content.find_all("title")

def find_h1_tags(page_content):
	bs_content = bs(page_content, "html.parser")
	return bs_content.find_all("h1")

def find_h2_tags(page_content):
	bs_content = bs(page_content, "html.parser")
	return bs_content.find_all("h2")