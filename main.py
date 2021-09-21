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
import jsonpath
import requests
import json


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

browser.set_page_load_timeout(30)

# Click on API token
browser.find_element_by_id('ctl00_ctrl_LeftMenuCloud1_hlnkAPIToken').click()

token_name = "rest_api"


# Get token --> copy
# browser.find_element_by_xpath('//*[@id="gvAPIToken"]/tbody/tr[3]/td[5]/div/img').click()


browser.switch_to.active_element
elem = browser.find_element_by_id('txtViewToken').get_attribute('value')
# elem.send_keys('ctrl+a')
# auth = elem.send_keys('ctrl+c')
print(elem)



browser.quit()


# Authtoken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJBbWlnb1NvZnR3YXJlIiwic3ViIjoiT1BDWFJBUEkiLCJlbWFpbCI6ImFzc2lzdGFuY2VAYW1pZ28tc29mdHdhcmUuY29tIiwicm9sZSI6IkludGVncmF0b3IiLCJNUFQiOiJGYWxzZSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvaXNwZXJzaXN0ZW50IjoiVHJ1ZSIsImlhdCI6MTYzMjIxODI1MCwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy92ZXJzaW9uIjoiUHJvZHVjdGlvbiIsImV4cCI6MTk3NzgxODI1MCwiYXVkIjoiT1BDWFJBUEkiLCJMSUkiOiJUcnVlIiwiTElET1MiOiIwMDI1Mi03MDAwMC0wMDAwMC1BQTUzNSIsImV4cGlyZXNfYXQiOiIxOTc3ODE4MjUwIiwibmJmIjoxNjMyMjE4MjUwfQ.RaYGVNleM9bfnMJ-l6kjH6Y6VmlZkc-RGgHae1W7OUo'

# Server AuthToken
# Parameters = {
#     "AuthToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJBbWlnb1NvZnR3YXJlIiwic3ViIjoiT1BDWFJBUEkiLCJlbWFpbCI6ImFzc2lzdGFuY2VAYW1pZ28tc29mdHdhcmUuY29tIiwicm9sZSI6IkludGVncmF0b3IiLCJNUFQiOiJGYWxzZSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvaXNwZXJzaXN0ZW50IjoiVHJ1ZSIsImlhdCI6MTYzMjIxODI1MCwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy92ZXJzaW9uIjoiUHJvZHVjdGlvbiIsImV4cCI6MTk3NzgxODI1MCwiYXVkIjoiT1BDWFJBUEkiLCJMSUkiOiJUcnVlIiwiTElET1MiOiIwMDI1Mi03MDAwMC0wMDAwMC1BQTUzNSIsImV4cGlyZXNfYXQiOiIxOTc3ODE4MjUwIiwibmJmIjoxNjMyMjE4MjUwfQ.RaYGVNleM9bfnMJ-l6kjH6Y6VmlZkc-RGgHae1W7OUo",
#     "AuthUser": "admin",
#     "AuthPassword": "1234567a",
#     "AuthenticationType": "0"
# }
#
# url = "http://172.20.22.81/opcxrrestapi/Authentication/GetSessionAuthToken"
#
#
# response = requests.get(url, headers=Parameters)
# print(response.content)
# resp = response.json()
# Authkey = str(resp['AuthToken'])
#
# print ('Auth Token from Json Response for Server: ' +Authkey)

# ###############################################################################3
# table = browser.find_element_by_id('gvAPIToken')
# body = table.find_element_by_tag_name('tbody')
# rows = table.find_elements_by_tag_name('tr')
# cells = table.find_elements_by_tag_name('td')
#
# print(len(rows))
# print(len(cells))
#
# for i in range(len(rows)):
#         columns = rows[i].find_elements_by_tag_name("td")
#         for j in range(len(columns)):
#             if columns[j].text == token_name:
#                 columns[14].click()
#                 print(columns[j].text)

# # Enter name
# browser.find_element_by_id('tbName').send_keys(token_name)
#
# # Integrator token
# select_token = Select(browser.find_element_by_xpath('//*[@id="divSipTrunk"]/table/tbody/tr[1]/td[2]/table/tbody/tr[3]/td[2]/select'))
# # select by visible text
# select_token.select_by_visible_text('Integrator')
#
# #Generate Token
# browser.find_element_by_xpath('//*[@id="divSipTrunk"]/table/tbody/tr[1]/td[2]/table/tbody/tr[4]/td[2]/button').click()

# time.sleep(5)


# for i in range(len(rows)):
#     columns = rows.find_elements_by_xpath('//*[@id="gvAPIToken"]/tbody/tr['+str((i+1))+']')
#     if columns.text == token_name:
#         browser.find_element_by_xpath('//*[@id="gvAPIToken"]/tbody/tr['+(i+1)+']/td[5]/div/img').click()
#     for j in range(len(columns)):
#         if columns[j] == token_name:
#             columns[5].click()
#time.sleep(3)


# rowNo = ""
# Name = token_name
# row_size = len(rows)
# print(row_size)

# for i in range(row_size):
#     x = str(i)
#     row = body.find_element_by_xpath('//*[@id="gvAPIToken"]/tbody/tr['+i+']/td[5]/div/img')
#     if (rows.text == Name):
#         rowNo = str(i+1)
#         break
#     if (cell.text == token_name):
#         browser.find_element_by_xpath('//*[@id="gvAPIToken"]/tbody/tr['+cell+']/td[5]/div/img').click()
#     print(cell.text)


# header = table.find_elements_by_tag_name('th')
# for headerEl in header:
#     print(headerEl.text)

# print (header)
# print(len(table))

# for t in table:

# //*[@id="gvAPIToken"]/tbody/tr[1]/td[5]/div/img
# //*[@id="gvAPIToken"]/tbody/tr[3]/td[5]/div/img