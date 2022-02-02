from anime import search_anime, search_anime_episode_list, get_anime_episode


def main() -> None:

    """[summary]

    Main function to
    download anime.

    """

    try:
        # while True:
        anime = input("Enter anime name\n")
        if anime:

            print("Searching. Please wait...")

            anime_list = search_anime(anime)
            for (i, anime) in enumerate(anime_list):
                print(f"{i+1}. {anime['title']}")
            print("\n")

            anime_choice = int(input("Choose an anime by serial no.\n"))
            chosen_anime = anime_list[anime_choice - 1]
            print(f"You chose {chosen_anime['title']}. Searching for episodes...")

            episode_list = search_anime_episode_list(chosen_anime)
            for (i, episode) in enumerate(episode_list):
                print(f"{i+1}. {episode['title']}")

            episode_choice = int(input("Choose an episode by serial no.\n"))
            chosen_episode = episode_list[episode_choice - 1]
            print(f"You chose {chosen_episode['title']}. Searching...")

            episode_url, download_url = get_anime_episode(chosen_episode)
            print(
                f"To watch, ctrl+click on {episode_url}. To download, ctrl+click on {download_url}"
            )
    except KeyError as ke:
        raise ke


if __name__ == "__main__":
    main()
