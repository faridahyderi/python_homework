from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Set up Selenium with headless Chrome
options = Options()
options.add_argument('--headless')  # Run in headless mode
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open the OWASP Top 10 page
url = 'https://owasp.org/www-project-top-ten/'
driver.get(url)

# Give time for the page to load
time.sleep(3)

# Initialize a list to hold the vulnerability data
vulnerabilities = []

# Define XPath for extracting the vulnerability titles and links
xpath = "//li/a[contains(@href, 'Top10')]/strong"

# Find all elements matching the XPath
vuln_elements = driver.find_elements(By.XPATH, xpath)

# Loop through each element and extract the data
for vuln in vuln_elements:
    title = vuln.text
    link = vuln.find_element(By.XPATH, "..").get_attribute("href")  # Get the parent <a> href link
    vulnerabilities.append({
        "Title": title,
        "Link": link
    })

# Print the vulnerabilities to verify
print(vulnerabilities)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(vulnerabilities)

# Write the DataFrame to a CSV file
csv_file = 'owasp_top_10.csv'
df.to_csv(csv_file, index=False)

# Close the browser
driver.quit()

print(f"Data has been written to {csv_file}")
