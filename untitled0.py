import pandas as pd
#df = pd.read_csv("pokemon_data.csv")
#print(df.head(3))
#df.columns
#print(df[['Name','Type 1']])


D={"nom":["A","B","C"],"Age":[18,15,25]}

T1=pd.DataFrame(D)

#print(T1)

#print(T1.head(2))

#print(T1.tail(2))

#print(T1.sample(1))

#print(T1["nom"])

#print(T1.iloc[1:3])

#print(T1["nom"][1:3])
#print(T1.describe())

f1=T1["Age"]<20
#print(T1[f1])

f2=T1["nom"]=="B"
#print(T1[f2])
#et &
#print(T1[f1&f2])
# ou |
#print(T1[f1|f2])

s=[10000,5000,2000]
T1["Salaire"]=s
#print(T1)
T1.iloc[0]=["X",33,10500]
print(T1)
