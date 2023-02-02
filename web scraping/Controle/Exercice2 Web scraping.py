import requests
from bs4 import BeautifulSoup

req = requests.get('https://fr.wikipedia.org/wiki/Universit%C3%A9_au_Maroc')
soup = BeautifulSoup(req.text, "lxml")


#print(soup.h1)

#Question 1

#for sub_heading in soup.find_all('li'):
#    print(sub_heading.text)

#Question 2
l=["École","Faculté","Centre","Université"]
#for sub_heading in soup.find_all('li'):
#    for item in l:
#        if item in sub_heading.text:
#            print(sub_heading.text)

#Question 3
ecole=[]
faculte=[]
centre=[]
universite=[]
for sub_heading in soup.find_all('li'):
        if 'École' in sub_heading.text:
            ecole.append(sub_heading.text)
        if 'Faculté' in sub_heading.text:
            faculte.append(sub_heading.text)
        if 'Centre' in sub_heading.text:
            centre.append(sub_heading.text)
        if 'Université' in sub_heading.text:
            universite.append(sub_heading.text)
print('Ecole:')
for i in ecole:
    print(' *'+i)
print('Faculté:')
for i in faculte:
    print(' *'+i)
print('Centre:')
for i in centre:
    print(' *'+i)
print('Université:')
for i in universite:
    print(' *'+i)
        


