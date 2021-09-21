import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

# browser = webdriver.Chrome('C:\\Users\\Saad\\Downloads\\chromedriver_win32\\chromedriver')
browser = webdriver.Chrome("C:\\Users\\sarah.mahmood\\Downloads\\chromedriver_win32\\chromedriver.exe") #Webdriver browser
browser.get('http://172.20.22.81/OmniPCXRECORD/TenantAdmin.aspx') #Add a Website
# <<<<<<< HEAD
# =======

email = browser.find_element_by_name('ctrl_TenantAdmin1$txtUserName') #enter email_id
email.send_keys('admin')

password = browser.find_element_by_name('ctrl_TenantAdmin1$txtPassword') #enter password
password.send_keys('1234567a')

sign_in = browser.find_element_by_id('ctrl_TenantAdmin1_imgBtnLogin') #press submit button
sign_in.click()

# Click on API token
browser.find_element_by_id('ctl00_ctrl_LeftMenuCloud1_hlnkAPIToken').click()

# # Enter name
# browser.find_element_by_id('tbName').send_keys('rest_api')
#
# # Integrator token
# select_token = Select(browser.find_element_by_xpath('//*[@id="divSipTrunk"]/table/tbody/tr[1]/td[2]/table/tbody/tr[3]/td[2]/select'))
# # select by visible text
# select_token.select_by_visible_text('Integrator')
#
# #Generate Token
# browser.find_element_by_xpath('//*[@id="divSipTrunk"]/table/tbody/tr[1]/td[2]/table/tbody/tr[4]/td[2]/button').click()

# Get token --> copy
table = browser.find_elements_by_xpath('//*[@id="gvAPIToken"]/tbody/tr')
print(len(table))

for i in range:

# //*[@id="gvAPIToken"]/tbody/tr[1]/td[5]/div/img
# //*[@id="gvAPIToken"]/tbody/tr[3]/td[5]/div/img

browser.quit()
# >>>>>>> [Sarah]Restapi Put and post request. Main token generated.
