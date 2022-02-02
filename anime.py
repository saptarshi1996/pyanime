from config import (
    url_list,
)

from scraper import (
    search_scraper,
    scrape_episode_list,
    scrape_episode,
)


def get_episode_url(end_point: str) -> str:
    return url_list["base_url"] + end_point


def search_anime(search_term: str) -> list:
    try:

        search_url = url_list["search_url"] + search_term
        anime_list = search_scraper(url=search_url)
        return anime_list

    except Exception as e:
        raise e


def search_anime_episode_list(anime: dict) -> list:
    try:
        anime_page_url = get_episode_url(anime["url"])
        episode_list = scrape_episode_list(anime_page_url)
        return episode_list
    except Exception as e:
        print(e)
        return []


def get_anime_episode(episode: dict) -> list:
    try:

        episode_page_url = get_episode_url(episode["url"])
        episode_url, download_url = scrape_episode(episode_page_url)
        return get_episode_url(episode_url), get_episode_url(download_url)

    except Exception as e:
        print(e)
        return [None, None]
