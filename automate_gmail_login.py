from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class GmailLogin():

    def gmailsignin(self):

        baseUrl = "https://www.gmail.com"
        userId = "abcd@gmail.com" # add your email here
        password = "1234" # Add you password here

        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome()
        # Open the provided URL
        driver.get(baseUrl)
        driver.maximize_window()
        
        # Provide mail id and click next
        emailId = driver.find_element_by_name("identifier")
        emailId.clear()
        emailId.send_keys(userId)
        emailNextButton = driver.find_element_by_xpath("//*[@id='identifierNext']/content/span")
        emailNextButton.click()
        
        # The text field for Password takes a delta amount of time to appear within the Viewport.
        # Hence apart from just locating the xpath for Password field you have to induce some time
        # wait for password page to appear, then click it
        passwordField = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH,"//input[@name='password']")))
        passwordField.clear()
        # Provide pw and click next
        passwordField.send_keys(password)
        driver.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()

        # Click user's image at right-top corner
        userImage = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='gb']/div[2]/div[3]/div/div[2]/div/a")))
        userImage.click()
        userEmail = driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[6]/div[1]/div/div[2]")

        print(userEmail.text)
        if userId in userEmail.text:
            print("Pass")
        else:
            print("Failed!")
        print("Logged in successfully")


GmailLogin().gmailsignin()
