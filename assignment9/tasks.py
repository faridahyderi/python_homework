# Task 1
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


robots_url = "https://durhamcountylibrary.org/robots.txt"

driver.get(robots_url)

print("Contents of robots.txt:\n")
print(driver.page_source)

driver.quit()