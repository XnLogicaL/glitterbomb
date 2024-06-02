from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver

class main:
    def __init__(self):
        self.reports = 0
        self.browser = webdriver.Firefox()

        self.user_id = input("enter user id: ")
        self.reason_index = input("enter selection reason: ")
        self.reason_text = input("enter reason text: ")

        print("starting")

        while True:
            try:
                self.report()
            except KeyboardInterrupt:
                break
            except:
                sleep(30)
                continue

    def report(self):
        url = f"https://www.roblox.com/abusereport/userprofile?id={self.user_id}&redirecturl=https%3a%2f%2fwww.roblox.com%2fusers%2f{self.user_id}%2fprofile"

        self.browser.get(url)

        dropdown = self.browser.find_element(By.XPATH, "/html/body/div[3]/main/div[2]/div/div[2]/div[2]/form/div[1]/div/select")
        reason = self.browser.find_element(By.XPATH, "/html/body/div[3]/main/div[2]/div/div[2]/div[2]/form/div[2]/textarea")
        submit = self.browser.find_element(By.XPATH, "/html/body/div[3]/main/div[2]/div/div[2]/div[2]/form/div[3]/a")
        select = Select(dropdown)

        select.select_by_index(self.reason_index)
        reason.send_keys(self.reason_text)
        submit.click()

        self.reports += 1
        
        print(f"report #{self.reports} complete")

if __name__ == "__main__":
    main()
