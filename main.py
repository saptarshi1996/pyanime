from anime import (
    search_anime,
    search_anime_episode_list,
    get_anime_episode
)

def main() -> None:

    # while True:
    anime = input("Enter anime name\n")
    # anime = "my hero academia"
    if anime:

        print("Searching. Please wait...")

        anime_list: list = search_anime(anime)
        for (i, anime) in enumerate(anime_list):
            print(("{0}. {1}").format(i+1, anime['title']))
        print("\n")

        anime_choice: int = int(input("Choose an anime by serial no.\n"))
        chosen_anime: dict = anime_list[anime_choice-1]
        print("You chose {0}. Searching for episodes...".format(chosen_anime['title']))

        episode_list: list = search_anime_episode_list(chosen_anime)
        for (i, episode) in enumerate(episode_list):
            print(("{0}. {1}").format(i+1, episode['title']))

        episode_choice: int = int(input("Choose an episode by serial no.\n"))
        chosen_episode: dict = episode_list[episode_choice-1]
        print("You chose {0}. Searching...".format(chosen_episode['title']))

        episode_url, download_url = get_anime_episode(chosen_episode)
        print("To watch, ctrl+click on {0}. To download, ctrl+click on {1}".format(episode_url, download_url))


if __name__ == "__main__":
    main()
