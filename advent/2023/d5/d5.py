from sys import stdin

info = []

curr = list(map(int, input().split()[1:]))

for line in stdin:
    if line[0].isalpha():
        info.append(curr[:-1])
        curr = []
    else:
        curr.append(list(map(int, line.split())))
info.append(curr[:-1])

seeds = info[0]
seedrange = []
ind = 0
while ind < len(seeds):
    seedrange.append([seeds[ind], seeds[ind]+seeds[ind+1]-1])
    ind += 2


for nxtmap in info[1:]:
    newseedrange = []
    seedrange.sort(key=lambda x:x[0])
    nxtmap.sort(key=lambda x:x[1])
    for seed in seedrange:
        mapind = 0
        start, end = seed
        finished = False
        while mapind < len(nxtmap):
            deststart, mapstart, maplength = nxtmap[mapind]
            mapend = mapstart + maplength - 1
            shift = deststart - mapstart
            if mapstart > end:
                newseedrange.append([start, end])
                finished = True
                break
            if mapend < start:
                mapind += 1
                continue
            if mapstart <= start:
                if mapend >= end:
                    newseedrange.append([start+shift, end+shift])
                    finished = True
                    break
                else:
                    newseedrange.append([start+shift, mapend+shift])
                    start = mapend + 1
                    mapind += 1
                    continue
            else:
                newseedrange.append([start, mapstart-1])
                start = mapstart
                continue
        if not finished:
            newseedrange.append([start, end])

    seedrange = newseedrange
    print(len(seedrange))
print(sorted(seedrange)[0][0])

