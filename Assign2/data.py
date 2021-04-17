rlt = [dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(),
    dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(),
    dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(),
    dict(), dict()] 

for i in range(32):
    rlt[i]['YEAR'] = i + 1

keys = list()
content = list()

with open('./data.csv', 'r') as f:
    for line in f.readlines():
        lst = line.split(',')
        key = lst[0]
        del lst[0]

        for i in range(len(lst)):
            try:
                rlt[i][key] = int(lst[i])
            except:
                rlt[i][key] = float(lst[i])
print(rlt)
