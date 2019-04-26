import csv
import csv_read
import External_Internal
import json
import os
import pandas as pd
import string
import tags_search

hotel_websites = csv_read.column_to_list("valid_websites.csv", "valid_website")

hotel_names = [name.translate(str.maketrans('', '', " {}".format(string.punctuation)))\
		 for name in csv_read.column_to_list("valid_websites.csv", "name")]


# Files will be saved in the "websites" directory
current_directory = os.path.dirname(os.path.abspath(__file__))
websites_directory = os.path.join(current_directory, "websites")

tags = []

for name, website in zip(hotel_names, hotel_websites):
	External_Internal.getAllInternalLinks(website)
	internal_links = csv_read.column_to_list("internal.csv", "Urls")
	for internal_link in internal_links:
		if internal_link is None:
			continue
		tag_search = tags_search.TagSearch(internal_link)
		tag_search.fetch_page()
		tag_search.fetch_domain_name()
		tag_search.find_title_tags()
		tag_search.find_h1_tags()
		tag_search.find_h2_tags()
		tag_search.find_internal_a_tags()
		tag_search.find_title_tags()
		new_tags = tag_search.get_dict()
 
		tags.append(new_tags)

	file_path = os.path.join(websites_directory, "{}.json".format(name))

	with open(file_path, "w") as file:
		json.dump(tags, file, indent=2)