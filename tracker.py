from bs4 import BeautifulSoup
import requests
import smtplib

def send_email(message):
    mail_from = "ncsucarrental@gmail.com"
    mail_to = "araja2@ncsu.edu"

    username = "ncsucarrental"
    password = "testing@123"

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    #server.connect('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)

    server.sendmail(mail_from, mail_to , message)

def run():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    url = 'https://www.acs.ncsu.edu/php/coursecat/search.php'
    fall_2018 = '2188'

    course_list = [{'code':'501', 'strength':'0/70'},{'code':'522', 'strength':'0/110'}]

    for course in course_list:
        page = requests.post(url, data={'current_strm': fall_2018, 'subject':'CSC - Computer Science',
         'term': fall_2018,'course-inequality':'=' ,'course-number': course['code'] })

        k = page.json()

        soup = BeautifulSoup(k['html'], "html.parser")

        table = soup.find("table", {"class":"table section-table table-striped table-condensed"})
        table_row = table.find_all('tr')
        row_data = table_row[2].find_all('td')
        class_strength_status = row_data[3]
        print(class_strength_status)

        if course['strength'] not in class_strength_status:
            send_email(course['code'] + " course now open")
        else:
            send_email(course['code'] + " course still closed")

run()
