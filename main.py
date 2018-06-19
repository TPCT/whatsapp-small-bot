class whatsapp_bot:
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common import desired_capabilities
    from selenium.common.exceptions import ElementNotVisibleException
    from PIL import Image
    import warnings, os, time

    def loading_bar(self, length=100, time_sleep: 'millisecond' = 100, shape1='*', shape2='-', function_to_start_with=None):
        import time, sys
        progress_bar = ""
        for i in range(length + 1):
            if i % 2 == 0:
                progress_bar = "[%s%s][%s" % (i, '%', shape1 * i)
            else:
                progress_bar = "[%s%s][%s" % (i, '%', shape2 * i)
            sys.stdout.write(progress_bar)
            sys.stdout.flush()
            if i < length - 1:
                time.sleep(time_sleep * (1e-3))
                sys.stdout.write('\r')
                sys.stdout.flush()
            else:
                sys.stdout.write('\r')
                sys.stdout.flush()
                sys.stdout.write(progress_bar)
        sys.stdout.write(']')

    def __init__(self):
        self.logged = False
        self.driver_path = 'chromedriver.exe'
        self.contacts = []
        self.browser_creator(self.driver_path)
        self.login()
        self.upload('mgd', 'test.png', 'hello world this is a bot')
        self.upload('ziz', 'test.png', 'hello world this is a bot')
        self.upload('sarah', 'speedsssCapture.PNG', 'hello world this is a bot')
        self.upload('bro', 'test.png', 'hello world this is a bot')
        self.upload('maged', 'test.png', 'hello world this is a bot')

    def browser_creator(self, chrome_driver):
        try:
            from selenium import webdriver
            caps = self.desired_capabilities.DesiredCapabilities().CHROME
            caps["pageLoadStrategy"] = "normal"
            browser_options = webdriver.ChromeOptions()
            browser_options.add_argument('headless')
            browser_options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                         '(KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"')
            self.browser = webdriver.Chrome(executable_path=chrome_driver, chrome_options=browser_options,
                                            desired_capabilities=caps)
            self.browser.set_page_load_timeout(10000000000000000000000000000000000000000)
            self.browser.set_script_timeout(10000000000000000000000000000000000000000)
        except self.WebDriverException:
            print('[-] Invalid driver path. script will exit()')
            self.os._exit(1)

    def login(self):
        try:
            try:
                self.browser.get('https://web.whatsapp.com')
                while True:
                    try:
                        self.browser.find_element_by_css_selector('img[alt="Scan me!"')
                        self.browser.find_element_by_name('rememberMe')
                        break
                    except self.NoSuchElementException:
                        pass
                try:
                    self.WebDriverWait(self.browser, 10000000000).until(
                        lambda x: x.find_element_by_css_selector('img[alt="Scan me!"'))
                    self.WebDriverWait(self.browser, 10000000000).until(lambda x: x.find_element_by_name('rememberMe'))
                    self.browser.find_element_by_name('rememberMe').send_keys(self.Keys.SPACE)
                    while True:
                        try:
                            if not self.browser.find_element_by_id('progressbar').is_displayed():
                                break
                        except:
                            break
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
                except self.TimeoutException:
                    pass
                while True:
                    try:
                        self.WebDriverWait(self.browser, 15).until(lambda x: x.find_element_by_id('side'))
                        self.os.remove('qcode.png')
                        print('[+] You have logged in')
                        self.logged = True
                        break
                    except Exception as e:
                        print(e)
                        self.os.remove('qcode.png')
                        print('[-] session ended (restarting).')
                        self.login()
                        break
            except self.TimeoutException:
                pass
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
            contact_name ='l'
            last_contact = 'm'
            while True:
                try:
                    self.WebDriverWait(self.browser, 10000000000).until(lambda x:
                                                               x.find_element_by_css_selector('div[title="New chat"]'))
                    self.browser.find_element_by_css_selector('div[title="New chat"]').click()
                    search_box = self.browser.find_element_by_css_selector('input[title="Search contacts"]')
                    search_box.send_keys(self.Keys.ARROW_DOWN)
                    search_box.send_keys(self.Keys.ARROW_DOWN)
                    contact = self.browser.switch_to_active_element()
                    self.time.sleep(1)
                    break
                except Exception as e:
                    pass
            while True:
                time = 0
                if not self.browser.page_source.__contains__('Loading'):
                    if contact_name != last_contact and contact_name.__len__() > 0 and time < 3:
                        contact_name = contact.text.split('\n')[0]
                        if contact_name not in self.contacts:
                            self.contacts += [contact_name]
                        contact.send_keys(self.Keys.ARROW_DOWN)
                        contact = self.browser.switch_to_active_element()
                        last_contact = contact.text.split('\n')[0]
                        self.time.sleep(1)
                    else:
                        break
                    time += 1
                else:
                    pass
            try:
                self.browser.find_element_by_css_selector('span[data-icon="back-light"]').click()
            except:
                pass
            self.time.sleep(1)
        else:
            print('[-] Please Login First')
            self.os._exit(1)

    def send_message(self, username, message):
        if self.logged and self.contacts.__len__() != 0 and username in self.contacts and len(message.replace(' ', ''))\
                > 0:
            try:
                while True:
                    try:
                        self.WebDriverWait(self.browser, 10000000000).until(lambda x:
                                                                   x.find_element_by_css_selector(
                                                                       'div[title="New chat"]'))
                        self.browser.find_element_by_css_selector('div[title="New chat"]').click()
                        search_box = self.browser.find_element_by_css_selector('input[title="Search contacts"]')\
                            .send_keys(username)
                        self.time.sleep(1)
                        try:
                            self.WebDriverWait(self.browser, 10000000000).until(
                                lambda x: x.find_element_by_css_selector('span[title="%s"]' % username))
                        except self.TimeoutException:
                            print('Message Will Not be sent')
                        self.browser.find_element_by_css_selector('span[title="%s"]' % username).click()
                        message_box = self.browser.find_element_by_css_selector('div[dir="ltr"]')
                        message_box.send_keys(message)
                        message_box.send_keys(self.Keys.ENTER)
                        try:
                            self.browser.find_element_by_css_selector('span[data-icon="back-light"]').click()
                        except:
                            pass
                        print('[+] message sent to %s' % username)
                        break
                    except Exception as e:
                        print('Message Will Not be sent')
                        break
                        pass
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

    def upload(self, username, file_path, message=''):
        if self.logged:
            if self.os.path.isfile(file_path):
                try:
                    self.WebDriverWait(self.browser, 3).until(lambda x:
                                                               x.find_element_by_css_selector(
                                                                   'div[title="New chat"]'))
                    script = '''document.querySelectorAll('div[title="New chat"]')[0].style.visibility = "visible";'''
                    self.browser.execute_script(script)
                    self.browser.find_element_by_css_selector('div[title="New chat"]').click()
                    self.WebDriverWait(self.browser, 10000000000).until(lambda x:
                                                                    x.find_element_by_css_selector(
                                                                        'input[title="Search contacts"]'))
                    search_box = self.browser.find_element_by_css_selector('input[title="Search contacts"]')
                    search_box.send_keys(username)
                    search_box.send_keys(self.Keys.ARROW_DOWN)
                    self.time.sleep(1)
                    contact = search_box.send_keys(self.Keys.ARROW_DOWN)
                    self.browser.switch_to_active_element().click()
                    self.browser.find_element_by_css_selector('div[title="Attach"]').click()
                    self.time.sleep(1)
                    try:
                        self.browser.find_element_by_tag_name('li').find_element_by_tag_name('button').click()
                        self.time.sleep(1)
                        self.WebDriverWait(self.browser, 10000000000).until(lambda x:
                                                                   x.find_element_by_css_selector(
                                                                       'input[accept="image/*,video/mp4,video/3gpp"]'))
                        if self.os.path.isfile(file_path):
                            self.browser.find_element_by_css_selector('input[accept="image/*,video/mp4,video/3gpp"]'). \
                                send_keys(self.os.path.realpath(file_path))
                            self.WebDriverWait(self.browser, 10000000000).until(lambda x:
                                                x.find_element_by_css_selector('span[data-icon="send-light"]'))
                            if message.replace(' ', '').__len__() != 0:
                                self.browser.find_element_by_css_selector('div[dir="ltr"]').send_keys(message)
                            self.browser.find_element_by_css_selector('span[data-icon="send-light"]').click()
                            self.time.sleep(1)
                            script = '''document.querySelectorAll('div[title="New chat"]')[0].style.visibility = "visible";'''
                            self.browser.execute_script(script)
                            self.browser.find_element_by_css_selector('div[title="New chat"]').click()
                    except self.TimeoutException:
                        print('This Message Has Not Been Sent')
                    except Exception as e:
                        print('error', e)
                    self.browser.save_screenshot('test.png')
                    try:
                        self.browser.find_element_by_css_selector('span[data-icon="back-light"]').click()
                    except self.NoSuchElementException:
                        pass
                    print('[+] Uploaded to %s' % username)
                except Exception as e:
                    try:
                        self.browser.find_element_by_css_selector('span[data-icon="back-light"]').click()
                    except self.NoSuchElementException:
                        pass
                    print('Message has not sent: ' + str(e))
                    self.browser.save_screenshot('test.png')
            else:
                print('[+] This is unvalid file path')
        else:
            print('[-] Please Login First or specify vaild file.')
            self.os._exit(1)

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
                    choice = input("[1] for one friend message\n[2] for all friends message\n[3] Upload File\n[4] Logout\n[+] Please Choose (number): ")
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
                    elif choice == '3':
                        try:
                            print('[+] You selected Upload File for one friend service')
                            start = 1
                            for i in self.contacts:
                                print('[%s] %s' % (start, i))
                                start += 1
                            username = self.contacts[int(input('[+] Please Choice On of The Above (No.): ')) - 1]
                            file_path = input("[+] Please Enter File Path To Start Service: ")
                            self.upload(file_path, username)
                        except Exception as e:
                            print(e)
                            print('[-] Something went wrong. Please try again')
                    elif choice == '4':
                        if self.logged:
                            self.logout()
                            self.login()
                    else:
                        print('[-] Something went wrong. Please try again')
            except KeyboardInterrupt:
                self.os._exit(1)
        else:
            print('[+] Plese Login First')
            self.service_start()


whatsapp_bot()
