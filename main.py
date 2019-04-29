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

if not os.path.exists(websites_directory):
    os.makedirs(websites_directory)

tags = []

for name, website in zip(hotel_names, hotel_websites):
	External_Internal.getAllInternalLinks(website)
	