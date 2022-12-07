
## trem-dmenuselect
-----------------

**dependemcies**
>dmenu
>transmission-remote
>zsh

on run presents a dmenu selection of running torrents, which can be selected for further action (stop, start, remove).



## yts v0.3b
-----------------

**dependemcies**
>curl
>transmission-remote-cli
>internet connection

terminal based scraper of YTS (https://yts.mx/). Now able to chagne search values (Date, rating, sort)
BASED ON SCRIPT BY Newman Sanchez (https://github.com/lr-tech)

**usage**
>yts [movie name]           search string is optional

BUGS: changing language requires additional tweaking.
Otherwise still works.


## scraptpb.py
-----------------

**dependemcies**
>python
>requests
>os
>json
>urllib
>transmission-remote

**usage**
>python scraptpb.py [name]    general search
>python scraptpb.py                  top 100 movies

scraps tpb for top movie torrents, returns size seeders leechers and name
sends magnet to transmission-remote for download


## brightness (unused)
-----------------

**dependemcies**
> xrandr

changes brightness of connected screen. brightness + (adds) brightness - (subtracts)

## wifi-dmenu (unused)
-----------------

dependencies: nmcli, dmenu

loads avaliable wifi networks for you to connect to

## yts-torrent (changed to yts)
-----------------

**dependemcies**
> dmenu
> transmission-remote

on run searches yts for new movies (In future, filters are to be implimented). Found movies can be
downloaded or their trailer watched through default browser ($BROWSER) (might be changed to mpv in the future)


## android-uninstaller
-----------------

**dependemcies**
> adb

simple bash script that searches and removes a package with adb
