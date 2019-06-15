from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os
import config

###########################################################

#enter the link to the website you want to automate login.
website_link="https://webtime2.paylocity.com/webtime/Employee"
#enter your company id
companyid=config.LOGIN_CONFIG['companyid']
#enter your login username
username=config.LOGIN_CONFIG['username']
#enter your login password
password=config.LOGIN_CONFIG['password']

###########################################################

#enter the element for company id input field
element_for_companyid="CompanyId"
#enter the element for username input field
element_for_username="Username"
#enter the element for password input field
element_for_password="Password"
#enter the element for submit button
element_for_submit="/html/body/div[1]/div[1]/div[2]/div/form/button"
#enter the element for clockin
element_for_clockin="ClockIn"
#enter the element for clockout
element_for_clockout="ClockOut"
#enter the element for StartLunch
element_for_startlunch="StartLunch"
#enter the element for EndLunch
element_for_endlunch="EndLunch"

###########################################################



browser = webdriver.Safari()	#for macOS users[for others use chrome vis chromedriver]
browser.get((website_link))

# wait 5 seconds to be safe in case the site is slow to load
print('browser opened')
time.sleep(5)

try:
  # fill in sign in form and log in
	companyfield = browser.find_element_by_name(element_for_companyid)
	companyfield.send_keys(companyid)	
	usernamefield = browser.find_element_by_name(element_for_username)
	usernamefield.send_keys(username)		
	passwordfield = browser.find_element_by_name(element_for_password)
	passwordfield.send_keys(password)
	signInButton = browser.find_element_by_xpath(element_for_submit)
	signInButton.click()
	print('logging in...')
	time.sleep(3)

	time_set = UPDATE_THIS_WITH_A_UNIX_EPOCH_TIME # unix epoch time to time you want to trigger the action: https://www.epochconverter.com/
	while int(time.time()) < time_set:
		time_difference = time_set - int(time.time())
		minutes_difference = math.floor(time_difference / 60)
		seconds_difference = time_difference - math.floor(time_difference / 60) * 60
		print('not time yet: ', minutes_difference, 'mins', seconds_difference, 'secs left')
		time.sleep(5)
  
  #### uncomment the pair of lines for the next action (i.e. right now it's set to click on the start lunch button)
	# clockInButton = browser.find_element_by_name(element_for_clockin)
	# clockInButton.click()
	startLunchButton = browser.find_element_by_name(element_for_startlunch)
	startLunchButton.click()
  # endLunchButton = browser.find_element_by_name(element_for_endlunch)
	# endLunchButton.click()
  # clockOutButton = browser.find_element_by_name(element_for_clockout)
	# clockOutButton.click()
	print('action done baby! time to get outta here...')

	#### to quit the browser uncomment the following lines ####
	time.sleep(3)
	browser.quit()
	time.sleep(1)
	browserExe = "Safari"
	os.system("pkill "+browserExe)
	print('browser process ended, botting completed.')
except Exception:
	#### This exception occurs if the element are not found in the webpage.
	print("Some error occurred")

	#### to quit the browser uncomment the following lines ####
	browser.quit()
	browserExe = "Safari"
	os.system("pkill "+browserExe)

