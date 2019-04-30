import csv
import csv_read
import External_Internal

#<<<<<<< HEAD
hotel_websites = csv_read.column_to_list("ibnahmadbello.csv", "valid_website")
#=======
#hotel_websites = csv_read.column_to_list("1000sites.csv", "valid_website")
#>>>>>>> 145252e91af0740979563e1bda939b07ed15e189

for website in hotel_websites:
	internal_links = External_Internal.getAllInternalLinks(website)
	External_Internal.save_csv(internal_links)
	
