# trem-dmenuselect


## dependemcies
>dmenu
>transmission-remote
>zsh

on run presents a dmenu selection of running torrents, which can be selected for further action (stop, start, remove).


# yts v0.3b

terminal based scraper of YTS (https://yts.mx/). Now able to chagne search values (Date, rating, sort)
BASED ON SCRIPT BY Newman Sanchez (https://github.com/lr-tech)

## dependemcies
>curl
>transmission-remote-cli
>internet connection

### usage
```bash
yts [movie name]           #search string is optional
```

### known issues
changing language requires additional tweaking.
Otherwise still works.


# scraptpb.py

scraps tpb for top movie torrents, returns size seeders leechers and name
sends magnet to transmission-remote for download
k
## dependemcies
>python
>requests
>os
>json
>urllib
>transmission-remote

### usage
```python
python scraptpb.py [name]           //general search
python scraptpb.py                  //top 100 movies
```



# brightness (unused)

changes brightness of connected screen. brightness + (adds) brightness - (subtracts)

## dependemcies
> xrandr


# wifi-dmenu (unused)

loads avaliable wifi networks for you to connect to

## dependencies
> nmcli
> dmenu


# yts-torrent (changed to yts)

on run searches yts for new movies (In future, filters are to be implimented). Found movies can be
downloaded or their trailer watched through default browser ($BROWSER) (might be changed to mpv in the future)

## dependemcies
> dmenu
> transmission-remote



# android-uninstaller

simple bash script that searches and removes a package with adb

## dependemcies
> adb
