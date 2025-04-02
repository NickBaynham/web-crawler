import requests
from bs4 import BeautifulSoup


def get_internal_links(target: str) -> list[str]:
    print('Target URL is', target)

    response = requests.get(target_url)
    response.raise_for_status()

    # Print the HTTP status code
    print("Status Code:", response.status_code)

    # Let's see the HTML
    print(response.text)

    # parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # collect all the links
    link_elements = soup.select("a[href]")
    print(len(link_elements), 'links found in the document')

    urls = set()
    for link_element in link_elements:
        url = link_element["href"]
        if url.startswith(target_url):
            print(url)
            urls.add(url)

    print(len(urls), 'urls found in the document')
    return list(urls)


target_url = "https://www.scrapingcourse.com/ecommerce/"
print('Target URL is', target_url)
links = get_internal_links(target_url)

# crawl the internal links
for link in links:
    internal_links = get_internal_links(link)
    print(len(internal_links), 'links found')
