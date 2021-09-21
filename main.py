import time
from selenium import webdriver
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
