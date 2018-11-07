def search_string(searched):
	query = set()
	f = open('crawled.txt','r')
	for lines in f :
		query.add(str(lines))
	f.close()
	for url in query:
		if searched in url.casefold():
			print(url)
		else:
			pass
		
	
search_string('diwali')
		