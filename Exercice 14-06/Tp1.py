from iteration_utilities import duplicates
import random
ch="UH50218932"
#print(len(ch[2:]))

def checkNumero(ch):
    i=True
    if ch[:2]=="UH":
        i=True
    else:
        i=False
        return i
    
    if ch[2:].isdigit():
        if len(ch[2:])==8:
            i=True
        else:
            i=False
            return i
    else:
        i=False 
        return i
    if i==True:
        return i

#print(checkNumero("UH50j1932"))
#c="1j35"
#print(c.isdigit())
li=["UH50218935","UH50618932","UH50616932","UH52258932","UH50218932","UH50218232","UH50182532"]

def checkList(Li):
    for item in Li:
        if not checkNumero(item):
            return False
    return True

print(checkList(li))

def checkDiff (Li):
    l=list(duplicates(Li))
    if len(l)>0:
        return False
    return True

print(checkDiff (li))

def plusGrand(ch1, ch2):
    if checkNumero(ch1):
        if checkNumero(ch2):
            if ch1[2:]>ch2[2:]:
                return True
    return False

print(plusGrand("UH50616933","UH50616932"))  

def present (Li, st):
    for item in Li:
        if st==item:
            return True
    return False

print(present (li,"UH50616932"))

def formeGroupe(Li, n):
    l=[]
    if 0<n<len(Li):
        l=random.sample(Li,n)
    else:
        l=Li
    return l

print(formeGroupe(li, 3))



    







    
