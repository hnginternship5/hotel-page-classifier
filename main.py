import csv
import csv_read
import External_Internal

hotel_websites = csv_read.column_to_list("ibnahmadbello.csv", "valid_website")

for website in hotel_websites:
	internal_links = External_Internal.getAllInternalLinks(website)
	External_Internal.save_csv(internal_links)
	
