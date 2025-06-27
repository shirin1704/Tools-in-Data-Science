import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited = set()
matching_files = []

def crawl(url):
    if url in visited:
        return
    visited.add(url)

    try:
        res = requests.get(url)
        res.raise_for_status()
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return

    soup = BeautifulSoup(res.text, "html.parser")
    links = soup.find_all("a", href=True)

    for link in links:
        href = link["href"]
        full_url = urljoin(url, href)

        # Skip parent directory links
        if href == "../":
            continue

        # Recurse into subdirectories
        if href.endswith("/"):
            crawl(full_url)
        elif href.endswith(".html"):
            filename = href.split("/")[-1]
            first_letter = filename[0].upper()
            if "I" <= first_letter <= "S":
                matching_files.append(full_url)

# Start crawling
root_url = "https://sanand0.github.io/tdsdata/crawl_html/"
crawl(root_url)

# Final count
print(f"\nFound {len(matching_files)} .html files starting with I–S")
