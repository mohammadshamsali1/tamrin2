import numpy as np

GPA=0
GPA1=0
Units=0
specifacations = []
name = input ("NAME=")
specifications.append(name)
number=int(input(A1))
karnameh= np.zeros((number,3),dtype=object)
for i in range (0 , number):
    print(1+1)
    karnameh[i,0]=input("name of the course =")
    karnameh[i,1]=input("number of units =")
    karnameh[i,2]=input("the page of the course =")
    GPA1=GPA1+int(karnameh[i,2])*int(karnameh[i,1])
    Units=Units+int(karnameh[i,1])
    GPA=GPA1/Units
    print("student name =",specifacations[0])
    print("number of lessons",number)
    print(karnameh)
    print("GPA",GPA)