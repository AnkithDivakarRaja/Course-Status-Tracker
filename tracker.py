from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
page = requests.post('https://www.acs.ncsu.edu/php/coursecat/search.php', data={'current_strm':'2188', 'subject':'CSC - Computer Science',
 'term':'2188','course-inequality':'=' ,'course-number':'501' })

k = page.json()

#print(k['html'])

soup = BeautifulSoup(k['html'], "html.parser")

#table = soup.find('table', attrs={'summary':'This table details the sections of CSC 501 based on the criteria submitted in the search form.'})
table = soup.find("table", {"class":"table section-table table-striped table-condensed"})
table_row = table.find_all('tr')
row_data = table_row[2].find_all('td')
current = row_data[3]
