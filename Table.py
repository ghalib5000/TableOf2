import sys
try:
    a =  sys.argv[1]
except:
    a = 2
try:
    n =  sys.argv[2]
except:
    n = 10

def table(a,n):
    
    i=1
    print("##### Table Of ",a," #####")
    while i<=int(n):
        print(a," X ",i," = ",int(a)*i)
        i+=1 
table(a,n)