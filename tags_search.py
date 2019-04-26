import External_Internal
from bs4 import BeautifulSoup as bs
import requests
import json

class TagSearch:
	"""
	Searches for tags on the web page
	:params: site_url as string
	"""
	def __init__(self, site_url):
		self.site_url = site_url
		self.page_content = None
		self.title_tags_text = None
		self.h1_tags_text = None
		self.h2_tags_text = None
		self.page_dict = None
		self.page_json = None

	def fetch_page(self):
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
		page_object = requests.get(self.site_url, headers=headers)
		self.page_content = page_object.content

	def find_title_tags(self):
		bs_content = bs(self.page_content, "html.parser")
		title_tags = bs_content.find_all("title")
		self.title_tags_text = [tag.text.strip() for tag in title_tags]

	def find_h1_tags(self):
		bs_content = bs(self.page_content, "html.parser")
		h1_tags = bs_content.find_all("h1")
		self.h1_tags_text  = [tag.text.strip() for tag in h1_tags]

	def find_h2_tags(self):
		bs_content = bs(self.page_content, "html.parser")
		h2_tags = bs_content.find_all("h2")
		self.h2_tags_text  = [tag.text.strip() for tag in h2_tags]

	def get_dict(self):
		self.page_dict = {"title":self.title_tags_text, "h1_tags":self.h1_tags_text, "h2_tags": self.h2_tags_text}
		return self.page_dict
