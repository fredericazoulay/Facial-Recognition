#https://www.crummy.com/software/BeautifulSoup/bs4/doc
from bs4 import BeautifulSoup
import requests
import os
import urllib
import csv

#source = requests.get('https://www.imdb.com/chart/top').text
source = requests.get('https://vivatechnology.com/speakers').text
soup = BeautifulSoup(source, 'lxml')

# TO PRINT WEB SITE
#print(soup.prettify())

# CODE TO SCRAP
#csv_file = open('imdb.csv', 'w')
csv_file = open('speakers.csv', 'w')
csv_writer = csv.writer(csv_file)
#csv_writer.writerow(['title', 'year', 'rating', 'image'])
csv_writer.writerow(['firstname', 'lastname', 'company', 'function'])

def importTopMovies():
    #tab = soup.find('tbody', class_='lister-list')
	#tab = soup.find('div', class_='wrapp-all-sections')
	tab = soup.find('div', class_='section-body')
    # for movie in tab.find_all('tr'):
	for movie in tab.find_all('span'):
	#for movie in tab.find('div', class_='card-speaker'):
		for movie2 in movie.find_all('strong'):
			print(movie2)
        # try:
			# csv_writer.writerow(['firstname', 'lastname', 'company', 'function'])
            # title = movie.find('td', class_='titleColumn').a.text
            # year = movie.find('span', class_='secondaryInfo').text
            # rating = movie.find('td', class_='ratingColumn imdbRating').text
            # image = movie.find('td', class_='posterColumn').a.img['src']
            # csv_writer.writerow([title, year, rating, image])
			# firstname = movie.find('span', class_='firstname').text
            # lastname = movie.find('span', class_='lastname').span.text
            # company = movie.find('span', class_='company').text
            # function = movie.find('span', class_='function').text
            # csv_writer.writerow([firstname, lastname, company, function])
			# csv_writer.writerow(['firstname', 'lastname', 'company', 'function'])
			# csv_writer.writerow([firstname])
        # except Exception as e:
            # raise ValueError('Error')

importTopMovies()