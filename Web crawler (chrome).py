from selenium import webdriver
from bs4 import BeautifulSoup
import pickle
import selenium.webdriver
import csv

# Set up the Selenium Chrome driver
#To send the request to chrome to open "site:youtube.com+openinapp"
driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q=site:youtube.com+openinapp&num=10000")

# Perform the search
search_query = ""
search_input = driver.find_element("name", "q")
search_input.send_keys(search_query)
search_input.submit()

# Wait for the search results to load
driver.implicitly_wait(100)

# Get the page source after the search
page_source = driver.page_source

# Close the browser
driver.quit()

# Parse the HTML page source using BeautifulSoup
#links scraper 
soup = BeautifulSoup(page_source, "html.parser")

# Find and extract the search links
search_results = soup.find_all("a")
links = []
for result in search_results:
        link = result.get("href")
        links.append(link)

# Print the search links
for i, link in enumerate(links, start=1):
    print(f"Link #{i}: {link}")

with open("links.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Link Number", "Link"])
    writer.writerows((link) for link in enumerate(links,start=1))

#selenium webdriver function error 
# driver = selenium.webdriver.Firefox()
# driver.get("https://www.google.com/search?q=site%3Ayoutube.com+openinapp&rlz=1C1CHBF_enIN992IN992&oq=site%3Ayoutube.com+openinapp&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg7MgYIAhBFGDwyBggDEEUYOjIGCAQQRRg8MgYIBRBFGDzSAQc3NDJqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8")
# pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))