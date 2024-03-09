# practice files with csv
file = open('songs.csv')
content = file.readlines()
#print(content[1])
i = 1
while(i<len(content)):
    line = content[i].strip()
    songData = line.split(',')
    print(songData[1], ", " + songData[2])
    i = i+1

