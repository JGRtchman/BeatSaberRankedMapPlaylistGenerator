import json,requests

url = 'https://raw.githubusercontent.com/andruzzzhka/BeatSaberScrappedData/master/scoreSaberScrappedData.json'
template = {'playlistTitle':None,'playlistAuthor':'ScoreSaber','songs':{}}


temp = {0:{},1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{},9:{},10:{}}
try:
    r = requests.get(url)
    songs_dict = r.json()
    for x in songs_dict:
        for y in songs_dict[x]:
            song_stars = y['stars']
            for i in range (11):
                if(song_stars >= i and song_stars <= i + 0.99) :
                    temp[i][x] = songs_dict[x]

    songs = []


    for x in temp:
        songs.append([])
        for y in temp[x]:
            songs[x].append({'songName':temp[x][y][0]['name'],'hash':temp[x][y][0]['id']})


    for x in range(len(songs)):
        if(x <= 9):
            playlist = template
            playlist['playlistTitle'] = 'RankedMaps' + str(x) +'-'+ str(x) +'.99'
            playlist['songs'] = songs[x]
            fw = open('RankedMaps_'+ str(x) +'-'+ str(x) +'.99.json','w')
            json.dump(playlist,fw,indent=4)
        else:
            playlist = template
            playlist['playlistTitle'] = 'RankedMaps' + str(x) +'-'
            fw = open('RankedMaps_'+ str(x) +'-.json','w')
            json.dump(playlist,fw,indent=4)

except requests.exceptions.RequestException as e:
    print(e)