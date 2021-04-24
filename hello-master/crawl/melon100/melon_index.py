from Melon import Melon
from pprint import pprint

melon = Melon()
melon.setLikecnt()

melon.setAlbumData()
melon.setSongOthers()
# pprint(melon.songs)  # QQQ
# pprint(melon.albums)

print("--------------")
melon.saveAlbum()
melon.saveSong()
melon.saveSongRank()
melon.saveArtists()
melon.saveSongArtists()
