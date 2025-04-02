import requests

target_url = "https://www.scrapingcourse.com/ecommerce/"
print('Target URL is', target_url)

response = requests.get(target_url)

# Print the HTTP status code
print("Status Code:", response.status_code)
