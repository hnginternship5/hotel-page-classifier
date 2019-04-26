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
		self.title_tags = None
		self.h1_tags = None
		self.h2_tags = None
		self.page_json = None

	def fetch_page(self):
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
		page_object = requests.get(self.siteUrl, headers=headers)
		self.page_content = page_object.content

	def find_title_tags(self):
		bs_content = bs(self.page_content, "html.parser")
		self.title_tags bs_content.find_all("title")

	def find_h1_tags(self):
		bs_content = bs(self.page_content, "html.parser")
		self.h1_tags = bs_content.find_all("h1")

	def find_h2_tags(pself):
		bs_content = bs(self.page_content, "html.parser")
		self.h2_tags = bs_content.find_all("h2")

	def to_json(self):
		tags = {"title":self.title_tags, "h1_tags":self.h1_tags, "h2_tags": self.h2_tags}
		self.page_json = json.dumps(tags, indent=4)

	def get_json(self):
		return self.page_json
