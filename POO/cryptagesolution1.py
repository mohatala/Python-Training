mp="De98nN$9@4D9"
i=0
x,y,z,t="","","",""
L,L2=[],[]
for c in mp:
    if c.isupper():
        x+=c+"("+str(i)+")"
    elif c.islower():
        y+=c+"("+str(i)+")"
    elif c.isdigit():
        z+=c+"("+str(i)+")"
    else:
        t+=c+"("+str(i)+")"
    i+=1
mp2=x+y+z+t
print(mp2)
    
i=0
for c in mp2:
    if c=="(":
        L.append(i)
    elif c==")":
        L2.append(i)
    i+=1
print(L,L2)

pos=[]
for i in range(0,len(L)):
    pos.append(int(mp2[L[i]+1:L2[i]]))
print(pos)

car=[]
car.append(mp2[0])

for i in L2:
    if i != L2[-1]:
        car.append(mp2[i+1])
print(car)

dd={}
for i in range(len(pos)):
    dd[pos[i]]=car[i]
print(dd)
ch=""
for i in sorted(dd.keys()):
    ch+=dd[i]
print(ch)
