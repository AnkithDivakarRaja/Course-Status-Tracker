from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path=r"chromedriver.exe")

browser.get('https://www.acs.ncsu.edu/php/coursecat/index.php')

browser.find_element_by_id('auto-subject').send_keys("CSC", Keys.ENTER)
browser.find_element_by_class_name("btn-success")

enroll_size = browser.find_element_by_xpath("//*[@id=\"CSC-501\"]/table/tbody/tr[1]/td[4]/text()")

print(enroll_size)
