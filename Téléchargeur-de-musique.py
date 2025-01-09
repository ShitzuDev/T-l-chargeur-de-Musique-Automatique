import os
import yt_dlp

# Fonction pour télécharger une musique depuis YouTube en recherchant un titre
def download_music(search_query, output_folder="Musiques"):
    """
    Télécharge une musique depuis YouTube en utilisant une recherche.
    :param search_query: Titre ou artiste pour la recherche sur YouTube.
    :param output_folder: Dossier où sauvegarder les musiques.
    """
    # Créer le dossier s'il n'existe pas
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_folder, "%(title)s.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "quiet": False,  # Affiche les détails de téléchargement
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Recherche et téléchargement de : {search_query}")
        try:
            ydl.download([f"ytsearch:{search_query}"])
            print(f"Musique téléchargée dans : {output_folder}")
        except Exception as e:
            print(f"Erreur lors du téléchargement : {e}")

# Programme principal
def main():
    print("=== Téléchargeur de Musique Automatique ===")
    print("Entrez le titre ou l'artiste de la chanson que vous voulez télécharger.")
    print("Tapez 'exit' pour quitter.")

    while True:
        search_query = input("\nEntrez le titre ou l'artiste (ou 'exit' pour quitter) : ").strip()
        if search_query.lower() == "exit":
            print("Merci d'avoir utilisé le téléchargeur de musique !")
            break

        # Télécharger la musique basée sur la recherche
        download_music(search_query)

# Lancer le programme
if __name__ == "__main__":
    main()
