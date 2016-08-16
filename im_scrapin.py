#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2

url = "http://www.imdb.com/search/title?title="


def qurl(query):
	words = len(query)
	url = "http://www.imdb.com/search/title?title="
	for i in range(0,words):
		if (i <= words and i>0):
			url += '+' + query[i]
			#print url
		else:
			url += query[i]
			#print url
	return url

query = raw_input("Enter the movie name: ").split(" ")
#print query
final_url = qurl(query)
#print final_url

content = urllib2.urlopen(final_url)
soup = BeautifulSoup(content, 'lxml')


#rating extraction
ratings_arr= []
for stuff in soup.findAll('div', {'class','ratings-imdb-rating'}):
	ratings_arr.append(stuff['data-value'])

ratings_arr = ratings_arr[:5]
#print ratings_arr

#title extraction
titles_arr = []
for titles in soup.findAll('h3', {'class', 'lister-item-header'}):
	titles_arr.append(titles.a.string)

titles_arr = titles_arr[:5]
p#rint titles_arr



#years extraction
years_arr = []
for years in soup.findAll('span', {'class', 'lister-item-year'}):
	years_arr.append(years.string)
years_arr = years_arr[:5]
#print years_arr

#printing out stuff

i=0
for titles in titles_arr:
	try:
		print ' > ' + titles + years_arr[i] + '  - ' + ratings_arr[i]
		i += 1
	except TypeError:
		print ' > ' + str(titles) + '(' +str(years_arr[i]) + ')' + '  - ' + str(ratings_arr[i])

raw_input("")