import random

boys = ['mohammad', 'sobhan', 'abdollah', 'kiya', 'mahdi', 'sajjad', 'homan', 'arman']
girls = ['mahtab', 'hane', 'harir', 'fateme', 'kiana', 'faezeh', 'minoo', 'mina', 'soghra']

married=[]
for i in boys:
    girl_index=random.randint(0,len(girls)-1)
    My_Dict={"Hasband":i,"Wife":girls[girl_index]}
    girls.remove(girls[girl_index])
    married.append(My_Dict)
    
for i in married:
    print(i)

