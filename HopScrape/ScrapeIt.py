import HTMLTableParser

hp = HTMLTableParser.HTMLTableParser()
URL = 'http://www.hopslist.com/hops/'
hopUrls = hp.parse_url(URL)

table = hp.parse_url(URL)[0][1] # Grabbing the table from the tuple
table.head()
