import csv 
import requests
request = requests.get("https://openlibrary.org/search.json?q=python")
response = request.json()

f = open("book.csv" , "w")
data = csv.writer(f)
header = data.writerow(["Book" , "Year" , "Author"])

for book in response["docs"]:
	title = book.get("title")
	year = book.get("first_publish_year")
	author = book.get("author_name")
	try:
		if (int(year) > 2000):
			data.writerow([title , year , author])
	except:
		pass
