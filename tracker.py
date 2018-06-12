from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(message):
    mail_from = "ncsucarrental@gmail.com"
    mail_to = "araja2@ncsu.edu"

    username = "ncsucarrental@gmail.com"
    password = "i@mbatman"

    msg = MIMEMultipart()
    msg['From'] = mail_from
    msg['To'] = mail_to
    msg['Subject'] = "Course status tracker"

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.ehlo()
    server.login(username, password)

    server.sendmail(mail_from, mail_to , msg.as_string())

def run():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    url = 'https://www.acs.ncsu.edu/php/coursecat/search.php'
    fall_2018 = '2188'
    msg = ''

    course_list = [{'code':'501', 'strength':'0/80'},{'code':'522', 'strength':'0/120'}]

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
            msg += course['code'] + " course now open.\n"
            msg += str(class_strength_status);
        else:
            print(course['code'] + " course still closed.\n")

    if msg:
        send_email(msg)

run()
