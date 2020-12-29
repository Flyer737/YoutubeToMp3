# YoutubeToMp3
Python3 script that makes downloading mp3 files from youtube with youtube-dl simpler.

# Python
* Use Python3
`sudo apt-get install python3`

# Youtube-dl Updated
* Remove Youtube-dl if already installed

`sudo apt-get remove -y youtube-dl`

* Install updated version of Youtube-dl
`sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl`

`sudo chmod a+rx /usr/local/bin/youtube-dl`

`hash -r`
