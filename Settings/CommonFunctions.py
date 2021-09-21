import time
import os, pypyodbc
from datetime import datetime
import platform
import string
from random import *
import random
from selenium.webdriver.android.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support.select import Select


class CommonFunctions():
    # webdriver = browser
    starttime = time.process_time()
    PrereqTestCasesStatusUpdate = False  # True or False
    SuccessMessage = "Test Case Passed Successfully"
    FailedMessage = "Failed"
    ExecutionDate = str(datetime.now().date())
    ExecutionTime = str(time.strftime("%H:%M:%S", time.localtime()))
    platformsystem = str(platform.system())
    platformrelease = str(platform.release())
    WindowServer = str(platformsystem + platformrelease)
    SystemUser = os.getlogin()
    Domain = 'http://172.20.22.81/opcxrrestapi'
    authkey_server = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJBbWlnb1NvZnR3YXJlIiwic3ViIjoiT1BDWFJBUEkiLCJlbWFpbCI6ImFzc2lzdGFuY2VAYW1pZ28tc29mdHdhcmUuY29tIiwicm9sZSI6IkludGVncmF0b3IiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL2lzcGVyc2lzdGVudCI6IlRydWUiLCJpYXQiOjE2MzIyOTE2MDcsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IlByb2R1Y3Rpb24iLCJleHAiOjE2MzI1OTE2MDcsImF1ZCI6Ik9QQ1hSQVBJIiwiTElJIjoiVHJ1ZSIsIlVOU1QiOiJhZG1pbiIsIlVUWVBFIjoiU2VydmVyIiwiU0lURUNPREUiOiJDb25maWciLCJMSURPUyI6IjAwMjUyLTcwMDAwLTAwMDAwLUFBNTM1IiwiTVBUIjoiRmFsc2UiLCJleHBpcmVzX2F0IjoiMTYzMjU5MTYwNyIsIlJUQiI6IkZhbHNlIiwiZXhwaXJlc19taW51dGVzIjoiNTAwMCIsIm5iZiI6MTYzMjI5MTYwN30.5NmLhHNt_dEx82u2VorvfGfOMCfCepgGmd7xCazERWw'
    authkey_Site = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJBbWlnb1NvZnR3YXJlIiwic3ViIjoiT1BDWFJBUEkiLCJlbWFpbCI6ImFzc2lzdGFuY2VAYW1pZ28tc29mdHdhcmUuY29tIiwicm9sZSI6IkludGVncmF0b3IiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL2lzcGVyc2lzdGVudCI6IlRydWUiLCJpYXQiOjE2MzIyOTE4NjcsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IlByb2R1Y3Rpb24iLCJleHAiOjE2MzUyOTE4NjcsImF1ZCI6Ik9QQ1hSQVBJIiwiTElJIjoiVHJ1ZSIsIlVOU1QiOiJhZG1pbiIsIlVUWVBFIjoiU2l0ZSIsIlNJVEVDT0RFIjoiMDEwMDAxIiwiTElET1MiOiIwMDI1Mi03MDAwMC0wMDAwMC1BQTUzNSIsIk1QVCI6IkZhbHNlIiwiZXhwaXJlc19hdCI6IjE2MzUyOTE4NjciLCJSVEIiOiJGYWxzZSIsImV4cGlyZXNfbWludXRlcyI6IjUwMDAwIiwibmJmIjoxNjMyMjkxODY3fQ.okY0eQgydCQsR_fdLzfqiiyUqSv_CMgeeVG-vR4-LXM'
    authkey_Site_UserToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJBbWlnb1NvZnR3YXJlIiwic3ViIjoiT1BDWFJBUEkiLCJlbWFpbCI6ImFzc2lzdGFuY2VAYW1pZ28tc29mdHdhcmUuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL2lzcGVyc2lzdGVudCI6IlRydWUiLCJpYXQiOjE2Mjk5NzgwNjQsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IlByb2R1Y3Rpb24iLCJleHAiOjE2MzAwMTQwNjQsImF1ZCI6Ik9QQ1hSQVBJIiwiTElJIjoiVHJ1ZSIsIlVOU1QiOiJhZG1pbiIsIlVUWVBFIjoiU2l0ZSIsIlNJVEVDT0RFIjoiMDEwMDAxIiwiTElET1MiOiIwMDM3Ni0zMDczMC0zNTg4Ni1BQTMyMSIsIk1QVCI6IkZhbHNlIiwiZXhwaXJlc19hdCI6IjE2MzAwMTQwNjQiLCJSVEIiOiJGYWxzZSIsImV4cGlyZXNfbWludXRlcyI6IjYwMCIsIm5iZiI6MTYyOTk3ODA2NH0.n__Ju1ZPCcQ2V9zhX2gEe4APMRmLUc7I4-RZg3Dh--o'
    authuser = 'admin'
    authpassword = '1234567a'

    # Output Result File path
    OutPutFilePath = 'C:\\Users\\Administrator\\Desktop\\ExcelFile\\R2.5.0.2-OmniPCX RECORD REST API Automated Tests Sheet.xlsx'

    def Header(self, module, testcase, description):
        # Print Header
        print('------------------------------Starting------------------------------')
        print('------------------------------' + module + '------------------------------')
        print('------------------------------' + testcase + '------------------------------')
        print('------------------------------' + description + '------------------------------')

    # Tenant DB Connectivity
    def DBConnectivity(self):
        connection = pypyodbc.connect('Driver={SQL Server};'
                                      'Server=172.20.22.81\SQLEXPRESS;'
                                      'Database=OPCXR_Tenant_010001_ALE_Enterprise;'
                                      'uid=sa;pwd=sqlin1.')
        cursor = connection.cursor()

        return cursor

    # Config DB Connectivity
    def StringDBConnectivity(self):
        connection = pypyodbc.connect('Driver={SQL Server};'
                                      'Server=172.20.22.81\SQLEXPRESS;'
                                      'Database=OPCXR_Config_ALE_Enterprise;'
                                      'uid=sa;pwd=sqlin1.')
        cursor = connection.cursor()

        return cursor

    def GenrateValidIPString(self):
        '''Generate only integers Or IP Address'''
        first = str(randrange(100, 255))
        second = str(randint(1, 255))
        third = str(randint(1, 255))
        fourth = str(randint(1, 255))
        ValidIP = str('' + first + '.' + second + '.' + third + '.' + fourth + '')

        return ValidIP

    def GenrateSimpleStringLimit10(self):
        Simplestring = "".join([random.choice(string.ascii_uppercase) for x in range(6)])
        SimpleString = '' + Simplestring + 'test'

        return SimpleString

    def GenerateNumber(self):
        NumberString = str(randint(9999, 99999))

        return NumberString

    def GenrateValidPasswordString(self):
        upper = "".join([random.choice(string.ascii_uppercase) for x in range(3)])
        lower = "".join([random.choice(string.ascii_lowercase) for x in range(3)])
        numeric = str(randrange(10, 99))
        ValidPassword = upper + lower + numeric

        return ValidPassword

    def GenrateValidMac(self):
        first = str(randrange(10, 90))
        second = str(randint(10, 90))
        third = str(randint(10, 90))
        fourth = str(randint(10, 90))
        fifth = str(randint(10, 90))
        sixth = str(randint(10, 90))

        ValidMac = str('' + first + ':' + second + ':' + third + ':' + fourth + ':' + fifth + ':' + sixth + '')
        return ValidMac

    def GenrateDesc250(self):
        GenrateDesc250 = "".join([random.choice(string.ascii_uppercase) for x in range(255)])
        return GenrateDesc250

    def GenerateSpecialChar(self):
        SpecialChar = ''.join(
            [random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(10)])
        return SpecialChar

    def GenerateEmail(self):
        username = "".join([random.choice(string.ascii_lowercase) for x in range(8)])
        domain = "".join([random.choice(string.ascii_lowercase) for x in range(5)])

        Email = '' + username + '@' + domain + '.com'

        return Email

    def InitializeBrowser(self, webdriver):
        # Initialize Browser
        browser = webdriver.Chrome("C:\\Users\\sarah.mahmood\\Downloads\\chromedriver_win32\\chromedriver.exe")  # Webdriver browser
        browser.get('http://172.20.22.81/OmniPCXRECORD/TenantAdmin.aspx')

        return browser

    def SignInServer(self, browser):
        # browser.get('http://172.20.22.81/OmniPCXRECORD/TenantAdmin.aspx')

        email = browser.find_element_by_name('ctrl_TenantAdmin1$txtUserName')  # enter email_id
        email.send_keys('admin')

        password = browser.find_element_by_name('ctrl_TenantAdmin1$txtPassword')  # enter password
        password.send_keys('1234567a')

        sign_in = browser.find_element_by_id('ctrl_TenantAdmin1_imgBtnLogin')  # press submit button
        sign_in.click()

        return browser

    def ClickAPIToken(self, browser):
        # Click on API token
        browser.find_element_by_id('ctl00_ctrl_LeftMenuCloud1_hlnkAPIToken').click()

    def CreateNewTokenIntegrator(self, browser):

        token_name = "Integrator_token"

        # Get token --> copy
        table = browser.find_element_by_id('gvAPIToken')
        rows = len(table.find_elements(By.TAG_NAME, "tr"))
        x = 1
        while x < rows:
            col = browser.find_element_by_xpath("//*[@id='gvAPIToken']/tbody/tr[" + str(x) + "]/td[1]")
            if col.text.__contains__(token_name):
                browser.find_element_by_xpath("//*[@id='gvAPIToken']/tbody/tr[" + str(x) + "]/td[5]/div/img").click()
                print("Element Found to copy")
                break
            x += 1

        time.sleep(3)

        try:

            if browser.switch_to.active_element:
                Integrator_token = browser.find_element_by_id('txtViewToken').get_attribute('value')
                browser.find_element_by_id('btnCloseViewToken').click()


            else:

                # Enter name
                browser.find_element_by_id('tbName').send_keys(token_name)

                # Integrator token
                select_token = Select(browser.find_element_by_xpath('//*[@id="divSipTrunk"]/table/tbody/tr[1]/td[2]/table/tbody/tr[3]/td[2]/select'))
                # select by visible text
                select_token.select_by_visible_text('Integrator')

                # Generate Token
                browser.find_element_by_xpath('//*[@id="divSipTrunk"]/table/tbody/tr[1]/td[2]/table/tbody/tr[4]/td[2]/button').click()

                time.sleep(3)

                # Get token --> copy
                table = browser.find_element_by_id('gvAPIToken')
                rows = len(table.find_elements_by_tagname("tr"))
                x = 1
                while x < rows:
                    col = browser.find_element_by_xpath("//*[@id='gvAPIToken']/tbody/tr[" + str(x) + "]/td[1]")
                    if col.text.__contains__(token_name):
                        browser.find_element_by_xpath("//*[@id='gvAPIToken']/tbody/tr[" + str(x) + "]/td[5]/div/img").click()
                        print("Element Found to copy")
                        break
                    x += 1

                time.sleep(3)

                browser.switch_to.active_element
                Integrator_token = browser.find_element_by_id('txtViewToken').get_attribute('value')
                browser.find_element_by_id('btnCloseViewToken').click()
            # elem.send_keys('ctrl+a')
            # auth = elem.send_keys('ctrl+c')

        finally:
            print('Nothing')

            return Integrator_token

    # Generate User token
    def CreateNewTokenUser(self, browser):

        token_name = "Integrator_token"

        # Get token --> copy
        table = browser.find_element_by_id('gvAPIToken')
        rows = len(table.table.find_elements_by_tagname("tr"))
        x = 1
        while x < rows:
            col = browser.find_element_by_xpath("//*[@id='gvAPIToken']/tbody/tr[" + str(x) + "]/td[1]")
            if col.text.__contains__(token_name):
                browser.find_element_by_xpath("//*[@id='gvAPIToken']/tbody/tr[" + str(x) + "]/td[5]/div/img").click()
                print("Element Found to copy")
                break
            x += 1

        time.sleep(3)

        try:

            if browser.switch_to.active_element:
                User_token = browser.find_element_by_id('txtViewToken').get_attribute('value')
                browser.find_element_by_id('btnCloseViewToken').click()


            else:

                # Enter name
                browser.find_element_by_id('tbName').send_keys(token_name)

                # Integrator token
                select_token = Select(browser.find_element_by_xpath('//*[@id="divSipTrunk"]/table/tbody/tr[1]/td[2]/table/tbody/tr[3]/td[2]/select'))
                # select by visible text
                select_token.select_by_visible_text('User')

                # Generate Token
                browser.find_element_by_xpath('//*[@id="divSipTrunk"]/table/tbody/tr[1]/td[2]/table/tbody/tr[4]/td[2]/button').click()

                time.sleep(3)

                # Get token --> copy
                table = browser.find_element_by_id('gvAPIToken')
                rows = len(table.table.find_elements_by_tagname("tr"))
                x = 1
                while x < rows:
                    col = browser.find_element_by_xpath("//*[@id='gvAPIToken']/tbody/tr[" + str(x) + "]/td[1]")
                    if col.text.__contains__(token_name):
                        browser.find_element_by_xpath("//*[@id='gvAPIToken']/tbody/tr[" + str(x) + "]/td[5]/div/img").click()
                        print("Element Found to copy")
                        break
                    x += 1

                time.sleep(3)

                browser.switch_to.active_element
                User_token = browser.find_element_by_id('txtViewToken').get_attribute('value')
                browser.find_element_by_id('btnCloseViewToken').click()
            # elem.send_keys('ctrl+a')
            # auth = elem.send_keys('ctrl+c')

        finally:
            print('Nothing')

            return User_token


