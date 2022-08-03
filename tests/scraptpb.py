import requests
import os
import json
import urllib

# TODO
# add variety to url options
# allow for term search
# make trem silent


# adds trailing white spaces for better viewing
def numbers_and_whitespace(number,size):
    i=10**size
    space=""
    while (i > number):
        space+=" "
        i/=10
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
name=input("name:")
url="https://apibay.org/q.php?q="+urllib.parse.quote(name)+"&cat=0"
print(url)
page=requests.get(url).text
data=json.loads(page)

print("GB    | seeders | leechers | id | name")
print("----------------------------------------")
for x in range(0,10):
    size=int(data[x]['size'])/1073741824
    print(("%.3f" % size) + " | "+
            numbers_and_whitespace(data[x]['seeders'],6)+ " | "+
            numbers_and_whitespace(data[x]['leechers'],7)+ " | "+
            numbers_and_whitespace(x+1,1)+ " | "+
            data[x]['name'])

movie_id=int(input("enter movie id: "))
movie_id-=1

magnet=get_magnet(data[movie_id]['info_hash'],data[movie_id]['name'])

print(os.system("transmission-remote -a '%s'" % magnet))
