import requests
from bs4 import BeautifulSoup


# request the target URL
def crawler():
    while urls_to_visit:
        # get the page to visit from the list
        current_url = urls_to_visit.pop(0)
        response = requests.get(current_url)
        response.raise_for_status()
        print(response.text)

        # parse the HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # collect all the links
        link_elements = soup.select("a[href]")
        for link_element in link_elements:
            url = link_element["href"]

            # convert links to absolute URLs
            if not url.startswith("http"):
                absolute_url = requests.compat.urljoin(target_url, url)
            else:
                absolute_url = url

            # ensure the crawled link belongs to the target domain and hasn't been visited
            if (
                absolute_url.startswith(target_url)
                and absolute_url not in urls_to_visit
            ):
                urls_to_visit.append(url)


target_url = "https://www.scrapingcourse.com/ecommerce/"

# initialize the list of discovered URLs
urls_to_visit = [target_url]

# execute the crawler
crawler()
