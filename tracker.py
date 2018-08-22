from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(message):
	mail_from = "ncsucarrental@gmail.com"
	mail_to = ["araja2@ncsu.edu", "nsompal@ncsu.edu"]
	
	username = "ncsucarrental@gmail.com"
	password = "i@mbatman"
	
	for mail_id in mail_to:
		msg = MIMEMultipart()
		msg['From'] = mail_from
		msg['To'] = mail_id
		msg['Subject'] = "Course status tracker"
		
		msg.attach(MIMEText(message, 'plain'))
		
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.ehlo()
		server.login(username, password)
		
		server.sendmail(mail_from, mail_id , msg.as_string())

def run():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    url = 'https://www.acs.ncsu.edu/php/coursecat/search.php'
    fall_2018 = '2188'
    msg = ''

    course_list = [{'code':'501', 'section':'001', 'strength':'0/30', 'subject':'BUS - Business Management'}, {'code':'501', 'section':'001', 'strength':'0/80', 'subject':'CSC - Computer Science'},
	{'code':'522', 'section':'001', 'strength':'0/120', 'subject':'CSC - Computer Science'},{'code':'591', 'section':'002', 'strength':'0/45', 'subject':'CSC - Computer Science'},
	{'code':'515', 'section':'001', 'strength':'0/64', 'subject':'CSC - Computer Science'}]

    for course in course_list:
        page = requests.post(url, data={'current_strm': fall_2018, 'subject': course['subject'],
         'term': fall_2018,'course-inequality':'=' ,'course-number': course['code'] })

        k = page.json()

        soup = BeautifulSoup(k['html'], "html.parser")

        table = soup.find("table", {"class":"table section-table table-striped table-condensed"})
        table_row = table.find_all('tr')
        #Handle multiple sections
        if course['section'] == '001':
            row_data = table_row[2].find_all('td')
        else:
            row_data = table_row[3].find_all('td')
        			
        class_section = row_data[0]
        class_strength_status = row_data[3]
        print(class_strength_status)

        if course['strength'] not in class_strength_status:
            msg += course['subject'] + ", " + course['code'] + " :" + str(class_section) + " course now open.\n"
            msg += str(class_strength_status);
        else:
            print(course['subject'] + ", " + course['code'] + " :" + str(class_section) + " course still closed.\n")

    if msg:
        send_email(msg)

run()
