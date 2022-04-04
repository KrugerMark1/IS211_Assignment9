from bs4 import BeautifulSoup as bs
import requests

def get_super_bowl_champions(url): 
	site = requests.get(url)
	site_content = site.content

	soup = bs(site_content, 'html.parser') 

	table = soup.find_all('table', {'class': ['wikitable', 'sortable', 'jquery-tablesorter']})[1]

	data = []

	for row in table.find('tbody').find_all('tr'):

		try:

			game = row.find_all('td')[0].find('a').string 
			team = row.find_all('td')[2].find('a').string 

			new_data = {
				"game": game,
				"team": team
			}

			data.append(new_data)

		except:

			print('n/a')


	print(data)


def get_world_series_champions(url):
	site = requests.get(url)
	site_content = site.content

	soup = bs(site_content, 'html.parser') 

	table = soup.find_all('table', {'class': ['wikitable', 'sortable', 'plainrowheaders']})[0]

	data = []

	for row in table.find('tbody').find_all('tr'):

		try:

			year = row.find('th').find('a').string 

			team = row.find_all('td')[0].find('a').string 

			new_data = {
				"year": year,
				"team": team
			}

			data.append(new_data)

		except:

			print('n/a')

	print(data)


def main():
	super_bowl_url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
	world_series_url = "https://en.wikipedia.org/wiki/List_of_World_Series_champions"

	get_super_bowl_champions(super_bowl_url)
	get_world_series_champions(world_series_url)

if __name__ == '__main__':
	main()