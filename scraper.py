import requests
import lxml

from bs4 import BeautifulSoup, NavigableString
from requests.models import Response

from config import (
    USER_AGENT
)


def search_scraper(url) -> list:

    try:
        print(url)

        response: Response = requests.get(url, headers={ "User-Agent": USER_AGENT })
        soup: BeautifulSoup = BeautifulSoup(response.text, "lxml")

        items_ul = soup.find("ul", { "class": "items" })
        items_li = items_ul.children

        anime_list: list = []
        for li in items_li:
            if not isinstance(li, NavigableString):
                anime_url, anime_title = li.find("a")['href'], li.find("a")['title']
                anime_list.append({
                    "title": anime_title,
                    "url": anime_url,
                })

        return anime_list

    except Exception as e:
        print(e)
        return []


def scrape_episode_list(url: str) -> list:
    try:

        print(url)

        response: Response = requests.get(url=url, headers={ "User-Agent": USER_AGENT })
        soup: BeautifulSoup = BeautifulSoup(response.text, "lxml")

        # With this id. get the episode list.
        episode_page_ul = soup.find("ul", { "id": "episode_related" })
        episode_page_li = episode_page_ul.children

        episode_list: list = []
        for children in episode_page_li:
            try:
                if not isinstance(children, NavigableString):
                    episode_list.append({
                        "title": children.find("div", { "class": "name" }).text.replace(" ", ""),
                        "url": children.find("a")['href']
                    })
            except Exception as e:
                pass

        return episode_list
    
    except Exception as e:

        print(e)
        return []


def scrape_episode(url: str) -> list:
    try:

        print(url)

        episode_url, download_url = "", ""

        response: Response = requests.get(url=url, headers={ "User-Agent": USER_AGENT })
        soup: BeautifulSoup = BeautifulSoup(response.text, "lxml")

        episode_url = soup.find("iframe", { "id": "playerframe" })['src']
        download_url = episode_url.replace("/embed/", "/playlist/") + ".m3u8"

        return episode_url, download_url
    
    except Exception as e:

        return []
