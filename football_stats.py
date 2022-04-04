from bs4 import BeautifulSoup as bs
import urllib.request

def grab_football_stats(url):
	
	fp = urllib.request.urlopen(url)
	mybytes = fp.read()

	html_string = mybytes.decode("utf8")
	fp.close()

	soup = bs(html_string, 'html.parser') 

	top_20_players = []

	for i in range(0, 20):
		columns = soup.find_all("tr", {"class": "TableBase-bodyTr"})[i].find_all("td", {"class": "TableBase-bodyTd"})

		name = columns[0].find("span", {"class": "CellPlayerName--short"}).find("span").find("a").string.replace('\n', '').replace(' ', '')
		position = columns[0].find("span", {"class": "CellPlayerName-position"}).string.replace('\n', '').replace(' ', '')
		team = columns[0].find("span", {"class": "CellPlayerName-team"}).string.replace('\n', '').replace(' ', '')
		total_touchdowns = columns[8].string.replace('\n', '').replace(' ', '')

		new_player = {
			"Name": name,
			"Position": position,
			"Team": team,
			"Total Touchdowns": total_touchdowns
		}

		top_20_players.append(new_player)

	print(top_20_players)

def main():
	url = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/all/?sortcol=td&sortdir=descending"

	football_stats = grab_football_stats(url)

if __name__ == '__main__':
	main()