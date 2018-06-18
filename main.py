class whatsapp_bot:
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import NoSuchElementException
    from PIL import Image
    import warnings, os, time
    def __init__(self):
        self.logged = False
        self.contacts = []
        self.service_start()


    def browser_creator(self, chrome_driver=r'c:\TPCT\chromedriver.exe'):
        try:
            from selenium import webdriver
            browser_options = webdriver.ChromeOptions()
            browser_options.add_argument('headless')
            browser_options.add_argument('window-size=1920x1080')
            browser_options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                         '(KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"')
            self.browser = webdriver.Chrome(executable_path=chrome_driver, chrome_options=browser_options)
        except self.WebDriverException:
            print('[-] Invalid driver path. script will exit()')
            self.os._exit(1)

    def login(self):
        try:
            self.browser.get('https://web.whatsapp.com')
            while True:
                try:
                    self.WebDriverWait(self.browser, 60).until(lambda x: x.find_element_by_name('rememberMe'))
                    self.WebDriverWait(self.browser, 60).until(lambda x: x.find_element_by_css_selector('img[alt="Scan me!"'))
                    break
                except self.TimeoutException:
                    pass
            self.browser.find_element_by_name('rememberMe').send_keys(self.Keys.SPACE)
            self.browser.save_screenshot('whatsapp.png')
            while True:
                try:
                    self.browser.find_element_by_id('progressbar').is_displayed()
                except:
                    break
            element = self.browser.find_element_by_css_selector('img[alt="Scan me!"')
            x1 = element.location['x'] + element.size['width'] + 20
            y1 = element.location['y'] + element.size['height'] + 20
            self.Image.open('whatsapp.png').crop(
                (int(element.location['x'] - 20), int(element.location['y'] - 20), int(x1),
                 int(y1))).save('qcode.png')
            self.os.remove('whatsapp.png')
            self.os.startfile('qcode.png')
            print('[+] Please Use Your Qcode in Your Whatsapp App')
            while True:
                try:
                    self.WebDriverWait(self.browser, 15).until(lambda x: x.find_element_by_id('side'))
                    self.os.remove('qcode.png')
                    print('[+] You have logged in')
                    self.logged = True
                    break
                except:
                    self.os.remove('qcode.png')
                    print('[-] session ended (restarting).')
                    self.login()
                    break
        except KeyboardInterrupt:
            self.os._exit(1)

    def logout(self):
        if self.logged:
            self.browser.find_element_by_css_selector('div[title="Menu"]').click()
            self.browser.find_element_by_css_selector('div[title="Log out"').click()
            self.logged = False
            print('[+] You have logged out')
        else:
            print('[-] Please Login First')
            self.os._exit(1)

    def get_contacts(self):
        if self.logged:
            while True:
                try:
                    self.WebDriverWait(self.browser, 60).until(lambda x:
                                                               x.find_element_by_css_selector('div[title="New chat"]'))
                    self.browser.find_element_by_css_selector('div[title="New chat"]').click()
                    contacts_container = self.browser.find_element_by_css_selector('div[data-list-scroll-container="true"]')
                    self.browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', contacts_container)
                    self.contacts = sorted(list(set([i.find_element_by_css_selector('span[dir="auto"]').text for i in
                                                     self.browser.find_element_by_css_selector('div[data-tab="3"]').
                                                     find_elements_by_css_selector('div[tabindex="-1"]')])))
                    self.browser.find_element_by_css_selector('span[data-icon="back-light"]').click()
                    break
                except Exception as e:
                    pass
        else:
            print('[-] Please Login First')
            self.os._exit(1)

    def send_message(self, username, message):
        if self.logged and self.contacts.__len__() != 0 and username in self.contacts and len(message.replace(' ', '')) \
                > 0:
            try:
                self.browser.find_element_by_css_selector('div[title="New chat"]').click()
                contacts_container = self.browser.find_element_by_css_selector('div[data-list-scroll-container="true"]')
                self.browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', contacts_container)
                try:
                    self.WebDriverWait(self.browser, 60).until(
                        lambda x: x.find_element_by_css_selector('span[title="%s"]' % username))
                except self.TimeoutException:
                    print('Message Will Not be sent')
                self.browser.find_element_by_css_selector('span[title="%s"]' % username).click()
                message_box = self.browser.find_element_by_css_selector('div[dir="ltr"]')
                message_box.send_keys(message)
                message_box.send_keys(self.Keys.ENTER)
                try:
                    self.browser.find_element_by_css_selector('span[data-icon="back-light"]').click()
                except self.NoSuchElementException:
                    pass
                print('[+] message sent to %s' % username)
            except Exception as e:
                try:
                    self.browser.find_element_by_css_selector('span[data-icon="back-light"]').click()
                except self.NoSuchElementException:
                    pass
                print('Message has not sent: ' + str(e))
                self.browser.save_screenshot('test.png')
        else:
            print('[-] Please Login First')
            self.os._exit(1)

    def message_to_all(self, message):
        for i in self.contacts:
            self.send_message(i, message)

    def service_start(self):
        def title():
            import os
            os.system(
                'title TPCT whatsapp messaging bot Version 1' if os.name == 'nt' else
                '\x1b]2;TPCT whatsapp messaging bot Version 1\x07')

        title()

        def cls():
            import os
            os.system('cls' if os.name == 'nt' else 'clear')

        cls()

        title = """
           _             _                              ______         _   
          | |           | |                             | ___ \       | |  
__      __| |__    __ _ | |_  ___   __ _  _ __   _ __   | |_/ /  ___  | |_ 
\ \ /\ / /| '_ \  / _` || __|/ __| / _` || '_ \ | '_ \  | ___ \ / _ \ | __|
 \ V  V / | | | || (_| || |_ \__ \| (_| || |_) || |_) | | |_/ /| (_) || |_ 
  \_/\_/  |_| |_| \__,_| \__||___/ \__,_|| .__/ | .__/  \____/  \___/  \__|
                                         | |    | |                        
                                         |_|    |_|                                                                  
                                Th3 Professional Cod3r
        Github: https://github.com/TPCT
        Facebook: https://www.facebook.com/Taylor.Ackerley.9"""
        print(title)
        path = input(r'[+] Please Enter Chrome Driver Path (c:\TPCT\chromedriver.exe\ Press Enter): ')
        if self.os.path.isfile(path):
            try:
                self.browser_creator(path)
                self.login()
                self.get_contacts()
            except self.WebDriverException as e:
                print('[-] Invalid driver make sure you are using chrome driver . script will exit()')
                self.os._exit(1)
        else:
            print('[-] Invalid driver path. script will exit()')
            self.os._exit(1)
        pass
        if self.logged:
            try:
                while True:
                    choice = input("[1] for one friend message\n[2] for all friends message\n[3] Logout\n[+] Please Choose (number): ")
                    if choice == "1":
                        try:
                            print('[+] You selected message for one friend service')
                            start = 1
                            for i in self.contacts:
                                print('[%s] %s' % (start, i))
                                start += 1
                            username = self.contacts[int(input('[+] Please Choice On of The Above (No.): ')) - 1]
                            message = input("[+] Please Enter Message To Start Service: ")
                            self.send_message(username, message)
                        except Exception as e:
                            print(e)
                            print('[-] Something went wrong. Please try again')
                    elif choice == "2":
                        try:
                            message = input("[+] Please Enter Message To Start Service: ")
                            self.message_to_all(message)
                        except:
                            print('[-] Something went wrong. Please try again')
                    else:
                        print('[-] Something went wrong. Please try again')
            except KeyboardInterrupt:
                self.os._exit(1)
        else:
            print('[+] Plese Login First')
            self.service_start()


whatsapp_bot()
