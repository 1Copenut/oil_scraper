#!/usr/bin/python
# Trevor Pierce
# 2013.07.02
# Proven US Oil Reserves by Year, 1899-2010
# Source: http://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=RCRR01NUS_1&f=A

from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv

base_url = "http://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=RCRR01NUS_1&f=A"

soup = BeautifulSoup(urlopen(base_url).read())
barrels = soup.find_all("td")

with open("data/oil.csv", "w") as f:
	# Set up the CSV file with proper column names
	fieldnames = ("Decade", "Year 0", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5", "Year 6", "Year 7", "Year 8", "Year 9")
	
	# Using File I/O, write the column names and close the file
	output = csv.writer(f, delimiter=",")
	output.writerow(fieldnames)
	
	# Now we grab the data and make it happen
	for barrel in barrels:
		test = barrel.get_text().encode("utf-8").split("&nbsp;")
		# output.writerow(barrel.get_text().encode("utf-8"))
		# print test
		output.writerow(test)

	
	
print "Done writing CSV data"