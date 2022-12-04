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
print(tracks.shape)

#displays only the rows 10-20 of the 'name' and 'release date' column
print(album.iloc[10:21][['name', 'release_date']])

#---------------------data cleaning----------------------------
#columns in the album file deemed inconsequential for this assignment and thus dropped were: 
drop_cols_album = ['external_urls', 'href', 'images', 'release_date_precision', 'uri', 'available_markets']
album.drop(drop_cols_album, inplace=True, axis=1)

#columns in the tracks file deemed inconsequential for this assignment and thus dropped were:
drop_cols_tracks = ['analysis_url', 'available_markets', 'uri', 'preview_url']
tracks.drop(drop_cols_tracks, inplace=True, axis=1)

#no columns in the artists data set were inconsequential thus were not dropped.

#rename the id column to be consistent with the other files
album = album.rename(columns={'id': 'album_id', 'name': 'song_name'})
tracks = tracks.rename(columns={'id': 'track_id', 'name': 'track_name'})
artists = artists.rename(columns={'id': 'artist_id', 'name': 'artist_name'})

#check for duplicate id's: no duplicates
duplicate_ids_album =album[album.duplicated(subset='album_id')]
duplicate_ids_track =tracks[tracks.duplicated(subset='track_id')]
duplicate_ids_artist =artists[artists.duplicated(subset='artist_id')]
print(f"list of duplicate id's for album:\n {duplicate_ids_album}")
print(f"list of duplicate id's for tracks:\n {duplicate_ids_track}")
print(f"list of duplicate id's for artist:\n {duplicate_ids_artist}")

#map() function to replace '[]' values with NaN
def fill_genre(value):
  if value == '[]':
    return np.NaN
  else:
    return value
artists['genres'] = artists['genres'].map(fill_genre)


#This prints all the unique values of the lyrics column. These values are essentially paragraphs of the song lyrics. This would be very difficult to parse in excel or other programs because they are massive and clunky values with many different characters, words, etc. 
print(tracks['lyrics'].unique()) #Shows the unique values of the lyrics column
tracks.drop(['lyrics'], inplace=True, axis=1) #This drops the lyrics column
print(tracks.info()) #Displays the lyrics column had indeed been dropped

#---------------------------Joining the Data Sets-------------------------
#outer joins were used in this data set to ensure no data was lost. The NaN values would not affect future calculations for the purpose of this assignment and the increase in possible un-needed rows did not reduce performance which could happen in a much larger data sets where a 'clunky' data set would slow things down.
#Join artists and albums on the artist ID

artists_with_albums = pd.merge(artists, album, on='artist_id', how='outer')
print(artists_with_albums.shape)
print(artists_with_albums.head())

#join albums and tracks on the album_ID
albums_with_tracks = pd.merge(album, tracks, on='album_id', how='outer')
print(albums_with_tracks.shape)
albums_with_tracks.head()

#-------------------------------------------------------------------------- 
#Which artists appear the most times in the Artists data?
print(artists_with_albums[["artist_id", 'artist_name']].value_counts(ascending=False)) #various artists appear the most. Johann Sebastion Bach is the individual artist that appears the most. 

#Which artists have the highest 'artist_popularity' rankings? (list the top ten in descending order): ['Ariana Grande', 'Drake', 'Post Malone', 'XXXTENTACION', 'Ozuna', 'Khalid', 'Juice WRLD', 'Queen', 'Travis Scott', 'Anuel Aa']
artists.drop_duplicates(subset='artist_name', inplace=True)
print(artists[['artist_popularity', 'artist_name']].sort_values(by='artist_popularity', ascending=False).head(10))




