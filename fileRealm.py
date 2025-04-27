#Define a dictionary to store the liked songs and their artists
liked_songs = {
    "Luther": "Kendrick Lamar",
    "Self Control": "Frank Ocean",
    "Pastikan Riuh Akhiri Malammu": "Perunggu",
    "Biang Lara": "Perunggu",
    "Cincin": "Hindia",
}

#Function to display and write liked songs to a file
def write_liked_songs_to_file(songs, file_name):
    with open(file_name, 'w') as file:
        file.write("Liked Songs:\n")
        for song, artist in songs.items():
            file.write(f"{song} by {artist}\n")
    print(f"Successfully added liked songs to {file_name} ❤️")

#Write liked songs to a .txt file
write_liked_songs_to_file(liked_songs, "liked_songs.txt")