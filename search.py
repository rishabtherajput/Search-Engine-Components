def search_string(searched):
	modif_search = searched.replace(" ", "_")
	query = set()
	f = open('wikipedia\crawled.txt','r',encoding='latin-1')
	for lines in f :
		query.add(str(lines))
	f.close()
	for url in query:
		if modif_search in url.casefold():
			if 'en.' in url.casefold():
				print(url)
		else:
			pass
		
	
search_string('great comet')
		