from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from bs4 import BeautifulSoup
import requests

app = FastAPI()

# Enable CORS for any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api/outline", response_class=PlainTextResponse)
def get_country_outline(country: str = Query(..., description="Country name")):
    # Create Wikipedia URL
    wiki_url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
    
    # Fetch the Wikipedia page
    response = requests.get(wiki_url)
    if response.status_code != 200:
        return PlainTextResponse(f"Failed to fetch Wikipedia page for {country}", status_code=404)

    # Parse the page
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract all headings h1 to h6 in order
    headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    
    # Markdown outline
    outline = []
    
    for tag in headings:
        level = int(tag.name[1])
        text = tag.get_text(strip=True)
        if text:
            outline.append(f"{'#' * level} {text}")

    return "\n\n".join(outline)
