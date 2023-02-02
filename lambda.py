some_numbers_list= [1,2,3,87,40,49,303,34,32,98]
filtered_list = list(filter(lambda x: x > 10, some_numbers_list))
#print(filtered_list)

#Ex1-1
s=lambda x: x+15
print(s(5))
#EX1-2
m=lambda x,y: x*y
print(m(5,2))

#Ex2
tu=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
filtered_list = list(sorted(tu,key=lambda x: x[1]))
print(filtered_list)

#Ex Map

def carre(n):
    return n*n
nb = (1, 2, 3, 4)

result=map(carre,nb)
print(list(result))
