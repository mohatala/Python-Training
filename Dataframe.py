import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/21260/Desktop/Master/Python/dataset_dash.csv")
#print(df.head(3))

#df.columns
l=[]
for m in df.loc[:, 'PYTHON']:
        l.append(m)
l1=[df['PYTHON']]
print(l)

#Get specific Rows
#print(df.iloc[0:4])

# get specific row column 
#print(df.iloc[2,1])

# iterate data 
#for index,row in df.iterrows():
#    print(index,row['Name'])

# Search with Parametre
#print(df.loc[df['Type 1']=="Grass"])

# Statistiques

#print(df.describe())

#Tri Data
#print(df.sort_values(['Type 1','HP'],ascending=True))

# Graph Line With Matplotlib 
#Line 1
#x=[0,1,2,3,4]
#y=[0,2,4,2,8]
#plt.plot(x,y,label='2x',color='red',marker='.',linestyle='--')
#Line 2
#x2=np.arange(0,4.5,0.5)
#plt.plot(x2,x2**2,'b+--',label='X°2')

######
#plt.title('test Graph',fontdict={'fontname':'Comic Sans MS','fontsize':20})
#plt.xlabel('X axis',fontdict={'fontname':'Comic Sans MS','fontsize':20})
#plt.ylabel('Y Axis',fontdict={'fontname':'Comic Sans MS','fontsize':20})
#plt.legend()
#save grach as png
#plt.savefig('testgraph.png',dpi=300)

# Graph 2 
#labels=['A','B','C']
#values=[1,4,2]
#plt.bar(labels,values)
#plt.figure(figsize=(6,4))

#Graph gas Usa vs Gas Canada 

#df = pd.read_csv("gas_prices.csv")
#print(df)
#xusa=df.Year
#yusa=df.USA
#xca=df.Year
#yca=df.Canada
#plt.plot(xusa,yusa,'r.--',label="USA")
#plt.plot(xca,yca,'b.--',label="CANADA")
#for country in df:
 #   if country!='Year':
  #      plt.plot(df.Year,df[country],'.--')
    
    
#plt.title('Gas Prices USA vs CANADA')
#plt.xlabel('Year')
#plt.ylabel('Price $')
#plt.xticks(df.Year[::3])
#plt.legend()
#plt.savefig('gasgraph.png',dpi=300)
