"""
def solution(m, musicinfos):
    answer = '(None)'
    
    def makesec(t):
        m1=int(t[0]+t[1])
        s1=int(t[3]+t[4])
        m2=int(t[6]+t[7])
        s2=int(t[9]+t[10])
        return (m2-m1)*60 + s1+s2
    def titlelen(t):
        title=t.split(",")[2]
        return len(title)
    
    musicinfos=sorted(musicinfos,key=lambda x: (makesec(x),-titlelen(x)))
    
    print(musicinfos)
    prevtime=0
    for info in musicinfos:
        sec=makesec(info)
        title,music=info.split(",")[2],info.split(",")[3]
        div,mod=divmod(sec,len(music))
        newmusic=music*div+music[:mod]
        if mod<len(music) and music[mod]=="#":
            newmusic+="#"
        print(newmusic)
        if m in newmusic and not sec==prevtime:
            idx=-1
            while True:
                idx=newmusic.find(m,idx+1)
                if idx==-1:
                    break
                if idx+len(m)==len(newmusic):
                    answer=title
                    prevtime=sec
                    break
                if idx+len(m)<len(newmusic) and m[-1]=="#":
                    answer=title
                    prevtime=sec
                    break
                
                if idx+len(m)<len(newmusic) and m[-1]!="#" and not newmusic[idx+len(m)]=="#":
                    answer=title
                    prevtime=sec
                    break
            print(answer,prevtime)
    return answer
"""


def changecode(music_):
    music_ = music_.replace("C#", "c")
    music_ = music_.replace("D#", "d")
    music_ = music_.replace("F#", "f")
    music_ = music_.replace("G#", "g")
    music_ = music_.replace("A#", "a")
    return music_


def caltime(musicinfo_):
    starttime = musicinfo_[0]
    endtime = musicinfo_[1]
    hour = 1 * (int(endtime.split(":")[0]) - int(starttime.split(":")[0]))
    if hour == 0:
        total = int(endtime.split(":")[1]) - int(starttime.split(":")[1])
    else:
        total = 60 * hour + int(endtime.split(":")[1]) - int(starttime.split(":")[1])

    return total


def solution(m, musicinfos):
    answer = []
    m = changecode(m)
    for idx, musicinfo in enumerate(musicinfos):
        musicinfo = changecode(musicinfo)
        musicinfo = musicinfo.split(",")
        time = makesec(musicinfo)

        # 길이가 시간보다 더 긴 경우
        if len(musicinfo[3]) >= time:
            melody = musicinfo[3][0:time]
        else:
            # 시간을 계산해서 몫과 나머지로 계산
            # 다른 사람 풀이 : q, r = divmod(time,len(musicinfo[3]))
            a = time // len(musicinfo[3])
            b = time % len(musicinfo[3])
            melody = musicinfo[3] * a + musicinfo[3][0:b]
        # 노래가 melody에 포함되면 정답후보에 저장
        if m in melody:
            answer.append([idx, time, musicinfo[2]])
    # 정답이 있는 경우
    if len(answer) != 0:
        # time -> index 기준으로 정렬
        answer = sorted(answer, key=lambda x: (-x[1], x[0]))
        return answer[0][2]
    # 정답이 없는 경우
    return "(None)"
