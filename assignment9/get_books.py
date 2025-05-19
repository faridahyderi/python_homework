from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

options = Options()


# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.set_page_load_timeout(180)

# Load the webpage
url = 'https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart'
driver.get(url)

# Wait for <li> elements to be present
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.cp-search-result-item'))
)

# Initialize the list to hold results
results = []

# Get the list items
li_elements = driver.find_elements(By.CSS_SELECTOR, 'li.cp-search-result-item')

# Loop through each item
for li in li_elements:
    try:
        title = li.find_element(By.CSS_SELECTOR, 'h2.cp-title a span.title-content').text
    except NoSuchElementException:
        title = "Title not found"

    authors = [a.text for a in li.find_elements(By.CSS_SELECTOR, 'a.author-link')]
    author = '; '.join(authors) if authors else "Author not found"

    try:
        format_year_div = li.find_element(By.CSS_SELECTOR, 'div.cp-format-info span.display-info-primary')
        format_year_text = format_year_div.text
        format_text, year_text = format_year_text.split(" - ") if " - " in format_year_text else (format_year_text, "")
        format_year = f"{format_text} - {year_text}"
    except NoSuchElementException:
        format_year = "Format/Year not found"

    # Debug prints
    print("----")
    print("Title:", title)
    print("Author:", author)
    print("Format-Year:", format_year)

    results.append({
        'Title': title,
        'Author': author,
        'Format-Year': format_year
    })

# Create and display the DataFrame
df = pd.DataFrame(results)
print(df)

# Save to CSV
df.to_csv('get_books.csv', index=False)

# Save to JSON
import json
with open('get_books.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)


# Clean up
driver.quit()
