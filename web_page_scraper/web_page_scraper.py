import requests
from bs4 import BeautifulSoup
import string
import os

BASE_URL = "https://www.nature.com"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_user_input():
    """
    Get user input for number of pages and article type.

    Parameters:
    None

    Returns:
    tuple: (int, str) number of pages and article type
    """
    print("Enter number of pages:")
    pages = int(input())

    print("Enter article type:")
    article_type_input = input()

    return pages, article_type_input


def get_page_soup(page: int):
    """
    Fetch and parse a Nature page.

    Parameters:
    page (int): page number to fetch

    Returns:
    BeautifulSoup: parsed HTML of the page
    """
    url = f"{BASE_URL}/nature/articles?sort=PubDate&year=2022&page={page}"
    response = requests.get(url, headers=HEADERS)
    return BeautifulSoup(response.text, "html.parser")

def get_article_links(soup: BeautifulSoup, article_type: str):
    """
    Extract article URLs filtered by article type.

    Parameters:
    soup (BeautifulSoup): parsed page HTML
    article_type (str): type of article to filter

    Returns:
    list: list of article URLs
    """
    links = []

    articles = soup.find_all("article")

    for article in articles:
        span = article.find("span")
        if not span:
            continue

        if article_type not in span.text:
            continue

        link = article.find("a", href=True)
        if link:
            links.append(BASE_URL + link["href"])

    return links

def get_article_content(url: str):
    """
    Fetch article title and text content.

    Parameters:
    url (str): article URL

    Returns:
    tuple: (title, text) or (None, None)
    """
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1")
    body = soup.find("div")

    if not title or not body:
        return None, None

    return title.text.strip(), body.text.strip()

def clean_title(title: str):
    """
    Clean article title for safe filename usage.

    Parameters:
    title (str): raw title

    Returns:
    str: cleaned filename-safe title
    """
    return title.translate(
        str.maketrans("", "", string.punctuation)
    ).replace(" ", "_")

def save_article(page: int, title: str, text: str):
    """
    Save article text to file.

    Parameters:
    page (int): page number
    title (str): article title
    text (str): article content

    Returns:
    None
    """
    os.makedirs(f"Page_{page}", exist_ok=True)

    file_path = os.path.join(f"Page_{page}", f"{title}.txt")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

def main():
    """
    Main program execution.

    Parameters:
    None

    Returns:
    None
    """
    pages, article_type = get_user_input()

    for page in range(1, pages + 1):
        soup = get_page_soup(page)
        links = get_article_links(soup, article_type)

        for url in links:
            title, text = get_article_content(url)

            if not title or not text:
                continue

            cleaned = clean_title(title)
            save_article(page, cleaned, text)

    print("Saved all articles.")

if __name__ == "__main__":
    main()