import re as regex

ch="az12&$-A654B8"
print(ch)
arr=list(ch)
up=""
dig=""
low=""
sp=""
#Split the password to specific order
for i in range(len(ch)):
    if ch[i].isupper():
        up+=ch[i]+"("+str(i)+")"
    elif ch[i].isdigit():
        dig+=ch[i]+"("+str(i)+")"
    elif ch[i].islower():
        low+=ch[i]+"("+str(i)+")"
    else:
        sp+=ch[i]+"("+str(i)+")"
        
mpe=low+up+dig+sp
L,L2=[],[]        
print(mpe)
#get the indice of ()
ind=0
for c in mpe:
    if c=="(":
        L.append(ind)
    elif c==")":
        L2.append(ind)
    ind+=1
#print(L,L2)
#get the indice between ()
indices=[]
for f, b in zip(L, L2):
    indices.append(mpe[f+1:b])

#get the character after )
lettres=[]
lettresindice=[]
lettres.append(mpe[0])
j=1
for i in L2:
    if i<L2[-1]:
        y=mpe[i+1]
        lettres.append(y)

#print(lettres)
#append charatcter with indice
L3=[]
for f, b in zip(lettres, indices):
    L3.append(f)
    L3.append(int(b))

print(L3)
#split list to multiple lists with 2 values
def splitlist(l, n):
    for i in range(0, len(l), n): 
        yield l[i:i + n]

x = list(splitlist(L3, 2))
#print (x)

print("*****************************")
from operator import itemgetter
print(sorted(x, key=itemgetter(1)))
x1=[]
pass1=""
x1=sorted(x, key=itemgetter(1))
#print(x1)
for i in x1:
    pass1+=i[0]

print(pass1)






    



