import urllib.request
for i in range(20):
    for j in range(20):
        try:
            if(j < 7):
                f = urllib.request.urlopen(
                    "http://192.168.81.10/?ime=AI1&x="+str(i)+"&y="+str(j)+"&boja=F33")
            if (j < 14 and j >= 7):
                    f = urllib.request.urlopen(
                    "http://192.168.81.10/?ime=AI2&x=" + str(i) + "&y=" + str(j) + "&boja=33F")
            if (j >= 14):
                f = urllib.request.urlopen(
                    "http://192.168.81.10/?ime=AI3&x=" + str(i) + "&y=" + str(j) + "&boja=FFF")
        except:
            x = 0