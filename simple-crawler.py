import requests
from bs4 import BeautifulSoup

target_url = "https://www.scrapingcourse.com/ecommerce/"
print('Target URL is', target_url)

response = requests.get(target_url)
response.raise_for_status()

# Print the HTTP status code
print("Status Code:", response.status_code)

# Let's see the HTML
print(response.text)

# parse the HTML
soup = BeautifulSoup(response.text, "html.parser")
