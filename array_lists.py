# Define album Class

class Album:

    def __init__(self, albumName, numberOfSongs, albumArtist):
        self.albumName = albumName
        self.numberOfSongs = numberOfSongs
        self.albumArtist = albumArtist
    
    def __str__(self):
        return f"({self.albumName}, {self.albumArtist}, {self.numberOfSongs})"

# create list with 5 albums and print 

albums1 = []

albums1.append(Album("The Downward Spiral", 14, "NIN" ))
albums1.append(Album("Evil Empire", 11, "Rage Against the Machine"))
albums1.append(Album("Toxicity", 14, "System of a Down"))
albums1.append(Album("The Story of You", 10, "SATSANG"))
albums1.append(Album("A War Story Book I", 12, "Psycho Realm" ))

print("\nAlbums1 list:\n")
for album in albums1:
    print(album)


# sort list according to the number of songs
# use  lambda keyword instead of def to create a lambda function.
# lambda argument(s) : expression

albums1.sort(key=lambda x: x.numberOfSongs)
print("\nSorted Albums1 List, min songs to max songs:\n")
for album in albums1:
    print(album)

# swap position of element at position 1 & 2 of albums
# member position 2 & 3 as position one always 0
# assignment expression lst[i], lst[j] = lst[j], lst[i] 

albums1[1], albums1[2] = albums1[2], albums1[1]
print("\nSwapped Albums1, position 1 & 2 in full List:\n")
for album in albums1:
    print(album)

# create a new list called albums2 & add 5 albums

albums2 = []

albums2.append(Album("AlbumH", 4, "ArtistA"))
albums2.append(Album("AlbumD", 6, "ArtistK"))
albums2.append(Album("AlbumA", 4, "ArtistG"))
albums2.append(Album("AlbumE", 10, "ArtistF"))
albums2.append(Album("AlbumB", 9, "ArtistP"))

print("\nAlbums2 list:\n")
for album in albums2:
    print(album)

# copy albums 1 into albums 2, extent meth
# extend method ,copy elements of a list to another list
albums2.extend(albums1)  


# Add the following two elements to albums2: 
# ○ (Dark Side of the Moon, Pink Floyd, 9)
# ○ (Oops!... I Did It Again, Britney Spears, 16)

albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops!... I Did It Again", 16, "Britney Spears"))

# sort albums2 in alphabetical order according
# to AlbumName and print

albums2.sort(key=lambda x: x.albumName)
print("\nAlbums2 sorted list with appended items and albums1:\n")
for album in albums2:
    print(album)


# search for dark side of the moon and print index


album_search = "Dark Side of the Moon"
for index, album in enumerate(albums2):
    if album.albumName == album_search:
        print(f"\n'{album_search}' found at index {index} in Albums2 List.\n")
        break
else:
    print(f"\n'{album_search}' not found in Albums2 List.\n")