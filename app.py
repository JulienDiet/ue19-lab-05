import requests

# Configuration API
API_URL = "https://myanimelist.p.rapidapi.com/anime/top/all"
HEADERS = {
    "x-rapidapi-key": "bfd1f30ae0msh032d618bba13158p1e8492jsn1ea08ff93fc2",  # Clé API (non sécurisée ici)
    "x-rapidapi-host": "myanimelist.p.rapidapi.com"
}
QUERYSTRING = {"p": "1"}  # Page des résultats (Top 50)


def fetch_top_anime():
    """
    Fonction pour interroger l'API MyAnimeList et récupérer les données.
    """
    try:
        response = requests.get(API_URL, headers=HEADERS, params=QUERYSTRING)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")
        return None


def main():
    """
    Point d'entrée principal de l'application.
    """
    print("Récupération des 50 meilleurs animes sur MyAnimeList...")
    animes = fetch_top_anime()
    if animes:
        for anime in animes:
            print(f"- {anime['title']} (Score : {anime.get('score', 'N/A')})")
    else:
        print("Impossible de récupérer les données.")


if __name__ == "__main__":
    main()
