class whatsapp_bot:
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException
    from selenium.common.exceptions import WebDriverException
    from PIL import Image
    import warnings, os, time
    def __init__(self):
        self.logged = False
        self.contacts = []
        try:
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
        except KeyboardInterrupt:
            self.os._exit(1)

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
                    break
                except self.WebDriverException:
                    pass
            self.browser.find_element_by_name('rememberMe').send_keys(self.Keys.SPACE)
            self.browser.save_screenshot('whatsapp.png')
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
                    self.browser.save_screenshot('test.png')
                    self.contacts = sorted(list(set([i.find_element_by_css_selector('span[dir="auto"]').text for i in
                                            contacts_container.find_elements_by_css_selector('div[tabindex="-1"]')])))
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
                self.browser.find_element_by_css_selector('span[title="%s"]' % username).click()
                message_box = self.browser.find_element_by_css_selector('div[dir="ltr"]')
                message_box.send_keys(message)
                message_box.send_keys(self.Keys.ENTER)
                print('[+] message sent to %s' % username)
            except Exception as e:
                print('Message has not sent: ' + str(e))
                self.browser.save_screenshot('test.png')
        else:
            print('[-] Please Login First')
            self.os._exit(1)

    def message_to_all(self, message):
        for i in self.contacts:
            self.send_message(i, message)

whatsapp_bot()
