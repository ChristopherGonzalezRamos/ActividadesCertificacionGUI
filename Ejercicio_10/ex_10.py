fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        #idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1

#print(di)

#now we want to find the most common word
tmp = list()
for k,v in di.items():
        newt = (v,k)
        tmp.append(newt)

#print('Flipped', tmp)
tmp = sorted(tmp, reverse=True)
#print('Sorted', tmp[:5])

for v,k in tmp[:5]:
     print(k,v)