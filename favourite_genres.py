from collections import Counter

def favourite_genres(user_songs: dict, song_genres: dict) -> dict:
    """
    Time  : O()
    Space : O()
    """
    # EDGE CASE
    if not song_genres:
        return {user: [] for user in user_songs.keys()}

    # KEEP TRACK OF THE GENRE OF EACH SONG
    song_genre = dict()
    for genre, songs in song_genres.items():
        for song in songs:
            song_genre[song] = genre

    # KEEP TRACK USERS AND THEIR MOST POPULAR GENRE
    user_popular = dict()

    # MAP THE SONGS TO THEIR GENRES
    for user, songs in user_songs.items():
        user_songs[user] = Counter([song_genre.get(song) for song in songs])
        max_freq = max(user_songs[user].values())
        user_popular[user] = [genre for genre, freq in user_songs[user].items() if freq == max_freq]

    return user_popular

if __name__ == "__main__":
    print(favourite_genres(
        {
            "David": ["song1", "song2", "song3", "song4", "song8"],
            "Emma": ["song5", "song6", "song7"]
        },
        {
            "Rock": ["song1", "song3"],
            "Dubstep": ["song7"],
            "Techno": ["song2", "song4"],
            "Pop": ["song5", "song6"],
            "Jazz": ["song8", "song9"]
        }
    ) == {
              "David": ["Rock", "Techno"],
              "Emma": ["Pop"]
          })

    print(favourite_genres(
        {
            "David": ["song1", "song2"],
            "Emma": ["song3", "song4"]
        },
        {}
    ) == {
              "David": [],
              "Emma": []
          })
