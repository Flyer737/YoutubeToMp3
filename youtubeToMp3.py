#Linux support only... IDK how to use yt-dl on windows :( I'm sorry

'''
sudo apt-get remove -y youtube-dl
sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
hash -r
'''

import os

running = True

while running:
	url=input("URL from youtube ('exit' to exit):")
	if url !="exit":
		os.system("youtube-dl --extract-audio --audio-format mp3 "+str(url))
	else:
		running = False


exit()
