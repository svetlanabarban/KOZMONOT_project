from selenium import webdriver

#imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
driver.get("http://18.212.223.46:3000")

driver.maximize_window()

wd_wait = WebDriverWait(driver, 10)

logo = wd_wait.until(
    EC.visibility_of_element_located((By.XPATH, "//img[@class='logo-dark mx-auto']")))


#selecting sign in
wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Sign In')]")))

signin_option = driver.find_element_by_xpath("//*[contains(text(), 'Sign In')]")
signin_option.click()

#Email Details
email_input = driver.find_element_by_xpath("//input[@type='email']")
email_input.clear()
email_input.send_keys("svetlanabarban@yahoo.com")

#Password Details
password_input = driver.find_element_by_xpath("//input[@type='password']")
password_input.clear()
password_input.send_keys("Ss2101989")

#clicking sign button
wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))

sign_button = driver.find_element_by_xpath("//button[@type='submit']")
sign_button.click()

time.sleep(2)

#selecting Console
wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,' Console')]")))

console_option = driver.find_element_by_xpath("//span[contains(.,' Console')]")
console_option.click()

#selecting "Add New LS"
wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(.,'Add New Livestream')]")))

new_livestream_button = driver.find_element_by_xpath("//button[contains(.,'Add New Livestream')]")
new_livestream_button.click()

#Add data
#Name
Name_input = driver.find_element_by_xpath("//input[@id='id_name']")
Name_input.clear()
Name_input.send_keys("Facebook August Launch3")

#Date
Date_input = driver.find_element_by_xpath("//input[@id='id_date']")
Date_input.clear()
Date_input.send_keys("2022-08-25")


#Time
Time_dropdown = driver.find_element_by_xpath("//input[@class='rc-time-picker-input']")


#Channel
Channel_dropdown = driver.find_element_by_xpath("//select[@id='id_channel']")
Channel_dropdown_select = Select(Channel_dropdown)
Channel_dropdown_select.select_by_visible_text('Facebook')

#Adding invalid link
Link_input = driver.find_element_by_xpath("//input[@id='id_link']")
Link_input.clear()
Link_input.send_keys("facebook.com")


#clicking save ls
wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Save')]")))

save_ls = driver.find_element_by_xpath("//*[contains(text(), 'Save')]")
save_ls.click()

time.sleep(5)
driver.quit()