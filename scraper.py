import requests

from bs4 import BeautifulSoup, NavigableString
from requests.models import Response

from config import USER_AGENT


def search_scraper(url: str) -> list:

    """[summary]

    Get an url and search for matching names.

    Returns:
        [type]: [description]
    """

    try:
        print(url)

        # request to the url and wait for response.
        response = requests.get(url, headers={"User-Agent": USER_AGENT})
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        anime_ul = soup.find("ul", {"class": "items"})
        anime_li = anime_ul.children

        anime_list = []
        for li in anime_li:
            if not isinstance(li, NavigableString):
                anime_url, anime_title = li.find("a")["href"], li.find("a")["title"]
                anime_list.append(
                    {
                        "title": anime_title,
                        "url": anime_url,
                    }
                )

        return anime_list

    except Exception as e:
        print(e)
        return []


def scrape_episode_list(url: str) -> list:

    """[summary]

    Get list of episodes using
    anime url.

    Returns:
        [type]: [description]
    """

    try:

        print(url)

        response = requests.get(url=url, headers={"User-Agent": USER_AGENT})
        soup = BeautifulSoup(response.text, "html.parser")

        # With this id. get the episode list.
        episode_page_ul = soup.find("ul", {"id": "episode_related"})
        episode_page_li = episode_page_ul.children

        episode_list = []
        for children in episode_page_li:
            try:
                if not isinstance(children, NavigableString):
                    episode_list.append(
                        {
                            "title": children.find(
                                "div", {"class": "name"}
                            ).text.replace(" ", ""),
                            "url": children.find("a")["href"],
                        }
                    )
            except Exception as e:
                pass

        return episode_list

    except Exception as e:
        print(e)
        return []


def scrape_episode(url: str) -> list:

    """[summary]

    Get the anime link
    from the url.

    Returns:
        [type]: [description]
    """

    try:

        print(url)

        response = requests.get(url=url, headers={"User-Agent": USER_AGENT})
        soup = BeautifulSoup(response.text, "html.parser")

        episode_url = soup.find("iframe", {"id": "playerframe"})["src"]
        download_url = episode_url.replace("/embed/", "/playlist/") + ".m3u8"

        return episode_url, download_url

    except Exception as e:
        return []
