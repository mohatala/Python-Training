import os

#Chemin de ce script
#print(os.getcwd())


#renomer un fichier
#os.rename("Les Tables.txt",'Execution Sur Les Tables.txt')



os.chdir("D:\Projetpython")
print(os.getcwd())

print(os.path.isdir ("D:\Projetpython"))

print(os.path.isdir ("D:\Projetpython\restaurant"))

print(os.path.isfile ("D:\Projetpython\DataFrame.txt"))

for f in os.listdir("D:\Projetpython") :
    print(f)


print("Afficher les fichiers jpg dans un dossier")
for root, dirs, files in os.walk("D:\Projetpython"):
    
 # select file name
     for file in files:    
 # check the extension of files
         if file.endswith('.png'):
 # print whole path of files
             print(os.path.join(root, file))
