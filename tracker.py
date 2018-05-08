from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
page = requests.post('https://www.acs.ncsu.edu/php/coursecat/search.php', data={'current_strm':'2188', 'subject':'CSC - Computer Science',
 'term':'2188','course-inequality':'=' ,'course-number':'501' })

#result = requests.get("https://www.acs.ncsu.edu/php/coursecat/index.php")

c = page.content

print(c)
