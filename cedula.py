#!/usr/bin/env python

cedula=(raw_input("Numero de Cedula: "))

r=0
verificador=0
c=1
for i in cedula[0:9]:
    if c%2!=0:
        r=int(i)*2
        
        if r>9:
            for x in str(r):
                verificador+=int(x)
        else:
            verificador+=r
    else:
        verificador+=int(i)
    
    c+=1    
 
if verificador%10==0 and int(cedula[9])==0:
    print "Cedula Valida"
elif (10-(verificador%10))==int(cedula[9]):
    print "Cedula Valida"
else:
    print "Cedula Falsa"





