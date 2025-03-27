from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options=webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("exclude-switches",["enable-automation"])

driver=webdriver.Chrome(options)
driver.get("https://www.speedtest.net/")


#print("Before clicking:", len(driver.window_handles))
logo=driver.find_element(By.CLASS_NAME,"start-text")
logo.click()
#print("After clicking:", len(driver.window_handles))
time.sleep(50)
down=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
down_text=down.text

up=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
up_text=up.text


# Print the results
print(f"Download Speed: {down_text}")
print(f"Upload Speed: {up_text}")