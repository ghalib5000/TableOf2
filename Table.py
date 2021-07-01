import sys
try:
    n =  sys.argv[1]
except:
    n = 10

def table(n):
    const = int(2)
    i=1
    print("##### Table Of 2 #####")
    while i<=int(n):
        print(const," X ",i," = ",const*i)
        i+=1 
table(n)