

vote = [[2,12,0],[3,11,1],[2,10,-1],[2,15,1],[5,9,0]] 

def filmsVus(vote, i ):
    x=0
    for item in vote:
        if item[0]==i:
            if item[-1]!=-1:
                x+=1
            
    if x==0:
        return -1
    else:
        return x


#print(filmsVus(vote,2))

def plusAime(vote):
    f=0
    l=[]
    for v in vote:
        if v[-1]==1:
            l.append(v[1])
    max=l.count(l[0])
    f=l[0]
    for i in l:
        x=l.count(i)
        if x>max:
            f=i
            max=l.count(i)  
    return f

vote = [[2,12,0],[2,10,1],[3,11,1],[2,11,1],[5,11,1]] 
print(plusAime(vote))

def plusAimedict(vote):
    f=0
    l=[]
    for v in vote:
        if v[-1]==1:
            l.append(v[1])
    D=dict()
    l2=set(l)
    for i in l2:
        D[i]=l.count(i)  
    for c in D.keys():
        if D[c]==max(D.values()):
            return c
    

print(plusAimedict(vote))

def filmsAimes(vote,u):
    l=[]
    for v in vote:
        if v[0]==u:
            if v[-1]==1:
                l.append(v[1])
    if len(l)==0:
        return -1
    else:
        return l

print(filmsAimes(vote,2))

def filmsCommuns(vote,i,j):
    l=[]
    l1=[]
    for v in vote:
        if v[0]==i:
            if v[-1]==1:
                l.append(v[1])
        if v[0]==j:
            if v[-1]==1:
                l1.append(v[1])
    l3=list(set(l) & set(l1))
    return l3

print(filmsCommuns (vote,2,3))

User={1:"med",2:"sara",3:"imad",4:"morad"}

def afficheVote(vote,User):
    for u in User.keys():
        if filmsAimes(vote,u)!=-1:
            print(User[u],"aime les films: ",filmsAimes(vote,u))


afficheVote(vote,User)
print(User)
print(vote)
def supprimeVote(vote,User,i):
    
    if i in User:
        del User[i]
    for v in vote:
        if v[0]==i:
             vote.remove(vote.index(v))
        

supprimeVote(vote,User,2)
print(User)
print(vote)
    






    
