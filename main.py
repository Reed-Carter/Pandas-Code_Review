import pandas as pd
import numpy as np

album_file = "./data/spotify_spotify_albums.csv"
album = pd.read_csv(album_file, header=0, sep=',', lineterminator='\n')

artists_file = "./data/spotify_spotify_artists.csv"
artists = pd.read_csv(artists_file, header=0)

track_file = "./data/spotify_spotify_tracks.csv"
tracks = pd.read_csv(track_file, header=0)

#prints the first 5 rows of the corresponding files
print(f"The first 5 rows of the album file:\n{album.head()}\n")
print(f"The first 5 rows of the artists file:\n{artists.head()}\n")
print(f"The first 5 rows of the tracks file:\n{tracks.head()}\n")

#prints the last 5 rows of the corresponding files
print(f"The last 5 rows of the album file:\n{album.tail()}\n")
print(f"The last 5 rows of the artists file:\n{artists.tail()}\n")
print(f"The last 5 rows of the tracks file:\n{tracks.tail()}\n")

#.shape returns a tuple where the first value is the number of rows and the second value is the number of columns
print(album.shape)
print(artists.shape)
print(album.shape)

#displays only the rows 10-20 of the 'name' and 'release date' column
album.iloc[10:21][['name', 'release_date']]

#---------------------data cleaning----------------------------
#columns in the album file deemed inconsequential and dropped were: 
drop_cols_album = ['external_urls', 'href', 'images', 'release_date_precision', 'uri', 'available_markets']
album.drop(drop_cols_album, inplace=True, axis=1)

#columns in the tracks file deemed inconsequential were:
drop_cols_tracks = ['analysis_url', 'available_markets', 'uri', 'preview_url']
tracks.drop(drop_cols_tracks, inplace=True, axis=1)

#no columns in the artists data set were inconsequential thus were not dropped.

#rename the id column to be consistent with the other files
album = album.rename(columns={'id': 'album_id'})
tracks = tracks.rename(columns={'id': 'track_id'})
artists = artists.rename(columns={'id': 'artist_id'})

#check for duplicate id's: no duplicates
duplicate_ids_album =album[album.duplicated(subset='album_id')]
duplicate_ids_track =tracks[tracks.duplicated(subset='track_id')]
duplicate_ids_artist =artists[artists.duplicated(subset='artist_id')]
print(f"duplicate ids:\n {duplicate_ids_album}")
print(f"duplicate ids:\n {duplicate_ids_track}")
print(f"duplicate ids:\n {duplicate_ids_artist}")
#------------------------------------------------------------------

#map() function to replace '[]' values with NaN
def fill_genre(value):
  if value == '[]':
    return np.NaN
  else:
    return value
artists['genres'] = artists['genres'].map(fill_genre)
artists['genres'].unique()

