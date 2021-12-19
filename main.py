filename = "crime_scene.txt"
f = open(filename)
sumlist = []
datadict = {}
for line in f:
    line=line.split()
    for number in line:
        sumlist.append(number)
f.close()
Wmax = int(sumlist[0])
Tmax = int(sumlist[1])
N = int(sumlist[2])
datadict = {}

def recdatadict(dic,lenn):
    if lenn==-1:
        return
    dic[sumlist[lenn]]=[sumlist[lenn+1],sumlist[lenn+2],sumlist[lenn+3]]
    recdatadict(dic, lenn-4)
recdatadict(datadict,len(sumlist)-4)

lenn=len(list(datadict.values()))

def weights(max, i):
    if i == lenn:
        return 0, []
    if max - int(list(datadict.values())[i][0]) >= 0:
        value, mylist = weights(max - int(list(datadict.values())[i][0]), i + 1)
        value += int(list(datadict.values())[i][2])
        mylist.append(list(datadict.keys())[i])
    else:
        value = 0
        mylist = []
    donttakevalue, donttakelist = weights(max, i + 1)
    if value > donttakevalue:
        return value, mylist
    else:
        return donttakevalue, donttakelist

weight_ev_val , weight_list = weights(Wmax, 0)

def time(max, i):
    if i == lenn:
        return 0, []
    if max - int(list(datadict.values())[i][1]) >= 0:
        value, mylist = time(max - int(list(datadict.values())[i][1]), i + 1)
        value += int(list(datadict.values())[i][2])
        mylist.append(list(datadict.keys())[i])
    else:
        value = 0
        mylist = []
    donttakevalue, donttakelist = time(max, i + 1)
    if value > donttakevalue:
        return value, mylist
    else:
        return donttakevalue, donttakelist

time_evidence_value , timelist = (time(Tmax, 0))

def timeandweight(maxtime, maxweight, i):
    if i == lenn:
        return 0, []
    if maxtime - int(list(datadict.values())[i][1]) >= 0 and maxweight - int(list(datadict.values())[i][0]) >= 0:
        value, mylist = timeandweight(maxtime - int(list(datadict.values())[i][1]), maxweight - int(list(datadict.values())[i][0]), i + 1)
        value += int(list(datadict.values())[i][2])
        mylist.append(list(datadict.keys())[i])
    else:
        value = 0
        mylist = []
    donttakevalue, donttakelist = timeandweight(maxtime, maxweight, i + 1)
    if value > donttakevalue:
        return value, mylist
    else:
        return donttakevalue, donttakelist

timeandweight_evidence_value, timeandweightlist = timeandweight(Tmax, Wmax, 0)

lenweightlist=len(weight_list)
def sort_list (lst):
    for i in range(len(lst)):
        j=i
        while (j>0 and int(lst[j-1])>int(lst[j])):
            lst[j-1], lst[j] = lst[j], lst[j-1]
            j = j - 1
    return lst
sort_list(weight_list)
sort_list(timelist)
sort_list(timeandweightlist)

f1 = open("solution_part1.txt","w")
f1.write(str(weight_ev_val))
f1.close()
f1 = open("solution_part1.txt","a")
f1.write("\n")
def f1write(i,lenx):
    if i == lenx:
        return
    f1.write(str(weight_list[i])+" ")
    f1write(i+1, lenx)
    return
f1write(0,len(weight_list))
f1.close()

f2 = open("solution_part2.txt","w")
f2.write(str(time_evidence_value))
f2.close()
f2 = open("solution_part2.txt","a")
f2.write("\n")
def f2write(i,lenx):
    if i == lenx:
        return
    f2.write(str(timelist[i])+" ")
    f2write(i+1, lenx)
    return
f2write(0,len(timelist))
f2.close()

f3 = open("solution_part3.txt","w")
f3.write(str(timeandweight_evidence_value))
f3.close()
f3 = open("solution_part3.txt","a")
f3.write("\n")
def f3write(i,lenx):
    if i == lenx:
        return
    f3.write(str(timeandweightlist[i])+" ")
    f3write(i+1, lenx)
    return
f3write(0,len(timeandweightlist))
f3.close()
