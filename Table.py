import sys
n = sys.argv[1]

def table(n=10):
    const = int(2)
    i=1
    print("##### Table Of 2 #####")
    while i<=int(n):
        print(const," X ",i," = ",const*i)
        i+=1 
table(n)