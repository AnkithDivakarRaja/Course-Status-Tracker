# Course-Status-Tracker

Created a simple script to continiously monitor the NCSU CSC course website to monitor the class status. An email is sent to the configured mail if the class status is Open or Waitlisted. No action is taken if the class status is closed. 

## Python libraries
1. Requests 
2. BeautifulSoup
3. SMTP

## Deployment

The script is deployed on heroku server. The application runs every 10 mins to monitor the class status.
