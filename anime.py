from config import (
    url_list,
)

from scraper import (
    search_scraper,
    scrape_episode_list,
)


def search_anime(search_term: str) -> list:
    try:

        search_url: str = url_list['search_url']+search_term.replace(" ", "%20")
        anime_list: list = search_scraper(url=search_url)
        return anime_list

    except Exception as e:
        raise e


def get_episode_url(end_point: str) -> str:
    return url_list['base_url']+end_point


def search_anime_episode_list(anime: dict) -> list:
    try:
        anime_page_url: str = get_episode_url(anime['url'])
        episode_list: list = scrape_episode_list(anime_page_url)
        return episode_list
    except Exception as e:
        print(e)
        return []
