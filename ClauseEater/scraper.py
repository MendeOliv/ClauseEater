import requests
from bs4 import BeautifulSoup

def scrape_and_clean_text(url: str) -> str:
    """
    Fetches the HTML content from a URL, extracts the text, and cleans it.

    Args:
        url: The URL of the website to scrape.

    Returns:
        The cleaned text content of the page.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, 'html.parser')

        # Remove script and style elements
        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()

        # Get text and clean it
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        cleaned_text = '\n'.join(chunk for chunk in chunks if chunk)

        return cleaned_text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return ""
