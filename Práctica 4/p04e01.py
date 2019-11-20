a = int(input("Introduce un número "))
b = int(input("Introduce un número "))
c = int(input("Introduce un número "))
d = int(input("Introduce un número "))
e = int(input("Introduce un número "))

maxi=int
mini=int
if a>b and a>c and a>d and a>e:
    maxi=a
elif b>a and b>c and b>d and b>e:
    maxi=b
elif c>a and c>b and c>d and c>e:
    maxi=c
elif d>a and d>b and d>c and d>e:
    maxi=d
elif e>a and e>b and e>c and e>d:
    maxi=e
else:
    maxi=a

if a<b and a<c and a<d and a<e:
    mini=a
elif b<a and b<c and b<d and b<e:
    mini=b
elif c<a and c<b and c<d and c<e:
    mini=c
elif d<a and d<b and d<c and d<e:
    mini=d
elif e<a and e<b and e<c and e<d:
    mini=e
else:
    mini=a

print ("El mayor es ", maxi, " y el menor es ", mini)

    
    
    
    
