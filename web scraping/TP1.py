from bs4 import BeautifulSoup
import pandas as pd

with open('index.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

print(soup.title)
print(soup.title.name)
print(soup.title.string) 

print(soup.a)
print(soup.a.string) 
print(soup.a.attrs) 
print(soup.a['href'])

print(soup.h1)
print(soup.h1.attrs)
print(soup.h1['lang']) 
#del soup.h1['id']
print(soup.h1)
print(soup.p)

for sub_heading in soup.find_all('p'):
    print(sub_heading.text)

print(soup.p.b) 

soup.p.find_all('b')

print(soup.p.contents)
print(soup.p.prettify())
print(soup.p.contents[2])
print(soup.p.contents[1].string)
for child in soup.p.children:
    print(child.name) 

print(soup.p.parent.name)
for parent in soup.p.parents:
    print(parent.name)

print(soup.table)
print("**************************************")

l=[]
l1=[]
i=0
for sub_heading in soup.find_all('td'):
    i+=1
    if(i<=3):
        l.append(sub_heading.text)
    else:
        l1.append(sub_heading.text)

    
print("********************************")
#print (l)
#print (l1)
data={}

for f, b in zip(l, l1):
    data[f]=[b,l1[l1.index(b)+3]]

print(data)
 
df = pd.DataFrame(data)
 
# Print the output.
print(df)




