import requests
import os
import json
import urllib
import sys
import re

# TODO
# add variety to url options
# allow for term search
# make trem silent

# adds trailing white spaces for better viewing
def numbers_and_whitespace(number,size):
    i=size
    space=""
    while (i > len(str(number))):
        space+=" "
        i-=1
    return (str(number)+space)

#converts data to magnet link
def get_magnet(info_hash,name):
    starMag="magnet:?xt=urn:btih:"
    dn="&dn="
    endMag="&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2780%2Fannounce&tr=udp%3A%2F%2Fopen.demonii.com%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=http%3A%2F%2Fp4p.arenabg.com%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce"
    m=(starMag+
            str(info_hash)+
            dn+
            urllib.parse.quote(name)
            +endMag)
    return m

url="https://apibay.org/precompiled/data_top100_201.json"
if (len(sys.argv) > 1):
    url="https://apibay.org/q.php?q="+urllib.parse.quote(re.sub(r'^.*? ','',' '.join(sys.argv)))+"&cat=0.json"

page=requests.get(url).text
data=json.loads(page)

length=10
if (len(data) < 10 ):
    length=len(data)

print("GB      | seeders | leechers | id | name")
print("----------------------------------------")
for x in range(0,length):
    size=round(int(data[x]['size'])/1073741824,2)
    print(  numbers_and_whitespace( size,7)        + " | "+
            numbers_and_whitespace( data[x]['seeders'],7)   + " | "+
            numbers_and_whitespace( data[x]['leechers'],8)  + " | "+
            numbers_and_whitespace( x+1,2)                  + " | "+
            data[x]['name'])

movie_id=int(input("enter movie id: "))
movie_id-=1

magnet=get_magnet(data[movie_id]['info_hash'],data[movie_id]['name'])

print(os.system("transmission-remote -a '%s'" % magnet))
