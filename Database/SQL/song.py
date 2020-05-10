class Song:
    def __init__(self,title,artist,duration=0):
        self.title = title
        self.duration = duration
        self.artist = artist
"""docstrings and raw literals"""
# Check classes diversity functions from SongTim file
class Album:

    def __init__(self,name,year,artist= None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist = artist
        self.tracks = []
    def add_song(self,song,position = None):

        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position,song)
class Artist:
    """Basic class to store artist details
    Attributes:
        name (str) : Name of artist
        albums (list[Album]): a list of albums artists
    Methods:
        add_album = use to add new album to the artist"""
    def __init__(self,name):
        self.name = name
        self.albums = []
    def add_album(self,album):
        """add new album to the list

        args:
        album ( album ) : Album object to add album
        if album is present if will not be added again"""

        self.albums.append(album)

def find_object(field,object_list):
    for item in object_list:
        if item == field:
            return item
    return None


def load_data():
    new_artist = None
    new_album = None
    artist_list = []
    with open("albums.txt", "r") as albums:
        # test file consists Artist,Album,Year,Song
        for line in albums:
            artist, album, year, song = tuple(line.strip("\n").split("\t"))
            year = int(year)
            print("{}:{}.{}.{}".format(artist,album,year,song))

            if new_artist is None:
                new_artist = Artist(artist)
                artist_list.append(new_artist)

            elif new_artist.name != artist:
                new_artist = find_object(artist,artist_list)
                if new_artist is None:
                    new_artist = Artist(artist)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album,year,new_artist)
                new_artist.add_album(new_album)
            elif new_album != album:
                new_album = find_object(album,new_artist.albums)
                if new_album is None:
                    new_album = Album(album, year, new_artist)
                    new_artist.add_album(new_album)
            # create new song object and add current album's collection
            new_song = Song(song,artist)
            new_album.add_song(new_song)

            if new_artist is not None:
                if new_album is not None:
                    new_artist.add_album(new_album)
                artist_list.append(new_artist)

    return artist_list

def create_checkfile(artist_list):
    with open("checkfile.txt","w") as checkfile:
        for new_artists in artist_list:
            for new_album in new_artists.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artists,new_album,new_song),
                          file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))
    create_checkfile(artists)