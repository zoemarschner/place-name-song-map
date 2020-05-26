import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv

img_urls = ['https://i.scdn.co/image/ab67616d0000b273d658a02ba8931985bdc4e0da', 'https://i.scdn.co/image/ab67616d0000b273b3c2c19a4fba83cd6e686fbf', 'https://i.scdn.co/image/ab67616d0000b2732df258170ebd07a908487304', 'https://i.scdn.co/image/ab67616d0000b273e6d4b9568e8db7d34dcba857', 'https://i.scdn.co/image/ab67616d0000b27356892234c1f80792f2605416', 'https://i.scdn.co/image/ab67616d0000b273ff0d959e4e35c8a773566d1a', 'https://i.scdn.co/image/ab67616d0000b2734f623f7be3aa1e881e416a24', 'https://i.scdn.co/image/ab67616d0000b27392f4cbe7bb66d3d78cd277cd', 'https://i.scdn.co/image/ab67616d0000b273cedb9116d166152da073aa32', 'https://i.scdn.co/image/ab67616d0000b2734c799baaee10a82fb21ae853', 'https://i.scdn.co/image/ab67616d0000b2734637341b9f507521afa9a778', 'https://i.scdn.co/image/ab67616d0000b2739047d1240dc46757ea2ea6ed', 'https://i.scdn.co/image/ab67616d0000b273e4779902c28979c42f1d723c', 'https://i.scdn.co/image/ab67616d0000b273f9e4287413e2d23a72f75ba9', 'https://i.scdn.co/image/ab67616d0000b2734e1a27b390392ae8ba40cfc4', 'https://i.scdn.co/image/ab67616d0000b2735dc08a1f177fbec3ce382c1d', 'https://i.scdn.co/image/ab67616d0000b273ef063cb80508c55eb443a671', 'https://i.scdn.co/image/ab67616d0000b2737fefd7638044e6326aeea15d', 'https://i.scdn.co/image/ab67616d0000b2736408ace21d12296424e36720', 'https://i.scdn.co/image/ab67616d0000b273c69442acf5c297d76a3505f2', 'https://i.scdn.co/image/ab67616d0000b2736408ace21d12296424e36720', 'https://i.scdn.co/image/ab67616d0000b273effdc0be1317dd16d8330ada', 'https://i.scdn.co/image/ab67616d0000b2730077c76c91243916b0b74dce', 'https://i.scdn.co/image/ab67616d0000b273bdc4eb647ab4c1204df33d84', 'https://i.scdn.co/image/ab67616d0000b2732ea43a2351fb6a2a9964395f', 'https://i.scdn.co/image/ab67616d0000b273def14d37c91f14c736d8cad4', 'https://i.scdn.co/image/ab67616d0000b2730b7d612d050103d76a72f8e1', 'https://i.scdn.co/image/ab67616d0000b273b05d0a40d077863b2a68e684', 'https://i.scdn.co/image/ab67616d0000b27394718a1ac1bbcc6b762a68fe', 'https://i.scdn.co/image/ab67616d0000b2737656c03fcc99c618582b5e78', 'https://i.scdn.co/image/ab67616d0000b2731bd0a9134f5e2ab286da24d2', 'https://i.scdn.co/image/ab67616d0000b273a7054529bcdd1ea5dcb852bc', 'https://i.scdn.co/image/ab67616d0000b2731bd0a9134f5e2ab286da24d2', 'https://i.scdn.co/image/ab67616d0000b2739e16f54ce1b5f9e1d8196ba3', 'https://i.scdn.co/image/ab67616d0000b2730d574fb245f014d83a7accbe', 'https://i.scdn.co/image/ab67616d0000b273d5f86e2ed9a548e213030078', 'https://i.scdn.co/image/ab67616d0000b2730b48826f176815f7b05e79e0', 'https://i.scdn.co/image/ab67616d0000b273bf4ed2df35e0f3a81bec4991', 'https://i.scdn.co/image/ab67616d0000b273ef6b8e3464eb5ac09be99c0a', 'https://i.scdn.co/image/ab67616d0000b27311b2557f3e2e06b35ef76d4b', 'https://i.scdn.co/image/ab67616d0000b2739cca0d695187fbeed4ee301b', 'https://i.scdn.co/image/ab67616d0000b2738e8e52bed62065b140d159c4', 'https://i.scdn.co/image/ab67616d0000b2733516e840c9ef5d06d75db6b7', 'https://i.scdn.co/image/ab67616d0000b273dff85da64d2bb4152516169c', 'https://i.scdn.co/image/ab67616d0000b273867dfe7571b1fad24f526a2d', 'https://i.scdn.co/image/ab67616d0000b2733ef1207895b314d646f6a3b7', 'https://i.scdn.co/image/ab67616d0000b273aa3a7399971d902e90e71095', 'https://i.scdn.co/image/ab67616d0000b27369a70bf66111a5db2de970ab', 'https://i.scdn.co/image/ab67616d0000b273a2b1d3e73c66663c01351bcf', 'https://i.scdn.co/image/ab67616d0000b27312f44f2b67bdcbb44004690f', 'https://i.scdn.co/image/ab67616d0000b273f6ba839208d6643e26ef3dab', 'https://i.scdn.co/image/ab67616d0000b27309f8dd8bf944e66b585fe708', 'https://i.scdn.co/image/ab67616d0000b2738842e85e405d9de6d1e0395f', 'https://i.scdn.co/image/ab67616d0000b273eec5bf14fcf7c92ec8166027', 'https://i.scdn.co/image/ab67616d0000b2736c619c39c853f8b1d67b7859', 'https://i.scdn.co/image/ab67616d0000b273fd910d582980afe314abb0b8', 'https://i.scdn.co/image/ab67616d0000b273508ea36e79a29abae48518cf', 'https://i.scdn.co/image/ab67616d0000b273022b4010e20659300f42c375', 'https://i.scdn.co/image/ab67616d0000b273a0b4a5b132f8555362a7174d', 'https://i.scdn.co/image/ab67616d0000b2731fecb146ba8b138e29b069be', 'https://i.scdn.co/image/ab67616d0000b273760157a341740478f939ff9f', 'https://i.scdn.co/image/ab67616d0000b273b5f23f29e2a2f7f131bb6500', 'https://i.scdn.co/image/ab67616d0000b2734889c266ea81f9f8fcd1c78d', 'https://i.scdn.co/image/ab67616d0000b273ba7fe7dd76cd4307e57dd75f', 'https://i.scdn.co/image/ab67616d0000b2731ab82b0d56d519a1cc434c01', 'https://i.scdn.co/image/ab67616d0000b273c79b600289a80aaef74d155d', 'https://i.scdn.co/image/ab67616d0000b27317fc8da0cf9bb33bc9ccd647', 'https://i.scdn.co/image/ab67616d0000b273488e71189d307285437ad1e0', 'https://i.scdn.co/image/ab67616d0000b273b586d555c83bf5c4199aacc8', 'https://i.scdn.co/image/ab67616d0000b27309880a7b8636c5a0615dc0c8', 'https://i.scdn.co/image/ab67616d0000b273027bab9100a21254a1c82893', 'https://i.scdn.co/image/ab67616d0000b27360124a534f8f257e7c158613', 'https://i.scdn.co/image/ab67616d0000b2730ac8ef14095a928fcf5027a1', 'https://i.scdn.co/image/ab67616d0000b27324297b1358e21aece02b8ccc', 'https://i.scdn.co/image/ab67616d0000b273d8fb5b4308dc27f210064ef4', 'https://i.scdn.co/image/ab67616d0000b273406b5316a88bcfad345a4c26', 'https://i.scdn.co/image/ab67616d0000b2738bbe5ef9d7a21f60ea2c351b', 'https://i.scdn.co/image/ab67616d0000b273ec8be21d32e663885fbb244e', 'https://i.scdn.co/image/ab67616d0000b273013c4a4de0647eb128daefd8', 'https://i.scdn.co/image/ab67616d0000b273258225089decfb3d5c3718d3', 'https://i.scdn.co/image/ab67616d0000b2738842e85e405d9de6d1e0395f', 'https://i.scdn.co/image/ab67616d0000b2738842e85e405d9de6d1e0395f', 'https://i.scdn.co/image/ab67616d0000b273d8d8fc095c6b5192bf91848e', 'https://i.scdn.co/image/ab67616d0000b27312843952346aaa03f1f67970', 'https://i.scdn.co/image/ab67616d0000b273e58da07e9b95eefe571c2121', 'https://i.scdn.co/image/ab67616d0000b273ab34519ffbf3149eaabaf2a8', 'https://i.scdn.co/image/ab67616d0000b2735d3392c1c31e81a56a2d9f56', 'https://i.scdn.co/image/ab67616d0000b273edcd2c497498760055df358b', 'https://i.scdn.co/image/ab67616d0000b2738240d6cea0205babc6814007', 'https://i.scdn.co/image/ab67616d0000b273dfe0edd0bc3902eb0b0e81b5', 'https://i.scdn.co/image/ab67616d0000b273e58da07e9b95eefe571c2121', 'https://i.scdn.co/image/ab67616d0000b2733d9d867b880ebf840fceec69', 'https://i.scdn.co/image/ab67616d0000b2734e61f016b81ffe8a41149552', 'https://i.scdn.co/image/ab67616d0000b27318de81c180ffdccf44afa962', 'https://i.scdn.co/image/ab67616d0000b27395b5e9af7be3a79aa70ddfdf', 'https://i.scdn.co/image/ab67616d0000b273ee9efa0ab721c018cd340722', 'https://i.scdn.co/image/ab67616d0000b273b40a526d36c2705b7d0307f3', 'https://i.scdn.co/image/ab67616d0000b273aa3a7399971d902e90e71095', 'https://i.scdn.co/image/ab67616d0000b27395020a88d022c23d2ded6aed', 'https://i.scdn.co/image/ab67616d0000b273630e59c29fcbc0abd6f36630', 'https://i.scdn.co/image/ab67616d0000b273b755882aff53af60a50e05d5', 'https://i.scdn.co/image/ab67616d0000b27384e7e4beb620014e8a71ed08', 'https://i.scdn.co/image/ab67616d0000b2733c069472f0139c369fedeb5c', 'https://i.scdn.co/image/ab67616d0000b2737d214af8499aa95ad220f573', 'https://i.scdn.co/image/ab67616d0000b2738b9e7e4bb2ff70126be3c338', 'https://i.scdn.co/image/ab67616d0000b27344a84d4cc8ba4fd73617b79a', 'https://i.scdn.co/image/ab67616d0000b273c42417c3c04d168d4c508d5d', 'https://i.scdn.co/image/ab67616d0000b273d2f6e14bf85bf359f248aef6', 'https://i.scdn.co/image/ab67616d0000b2737aede4855f6d0d738012e2e5', 'https://i.scdn.co/image/ab67616d0000b2736d9ebb9cc11e5c16bbba1d1a', 'https://i.scdn.co/image/ab67616d0000b2732d642cf5a3bd5809164b1cc1', 'https://i.scdn.co/image/ab67616d0000b2736ce61113662ecf693b605ee5']

def get_songs():
	# set up spotipy
	sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

	img_urls = []
	# open csv
	with open('songs.csv') as csvfile:
		song_reader = csv.reader(csvfile, delimiter=",")
		skip = True
		for row in song_reader:
			# first row is header
			if skip:
				skip = False
				continue

			# construct search term (you can use BOOLEANS in spotify search!!!!)
			search_term = f'artist:"{row[1].split(",")[0]}" AND track:"{row[0]}"'

			# query for results
			results = sp.search(q=search_term, type="track")
			if len(results['tracks']['items']) < 1:
				print(f"COULDN'T FIND: {search_term}")
				results = sp.search(q=f'{row[0]} {row[1].split(",")[0]}', type="track")
				if len(results['tracks']['items']) < 1:
					print(f"STILL COULDN'T FIND: {search_term}")
					continue

			res = results['tracks']['items'][0] # take the first result
			img_url = res['album']['images'][0]['url'] # url of highest res img
			img_urls.append(img_url)

	print(img_urls)

# making my fun html page :)
html_imgs = []
for img in img_urls:
	html_imgs.append(f'<img src={img} style="width: 25vw">')

html = '''
<!DOCTYPE html>
<html>
<head>
	<title>ALBUMS!</title>
</head>
<body style="margin:0px">
	<div id="album_box" style="display: flex;flex-wrap: wrap;justify-content: space-evenly;align-content: space-evenly;">''' + "\n".join(html_imgs) + '''	</div>
</body>
</html>
'''

with open("albums.html", mode="w+") as html_file:
	html_file.write(html)