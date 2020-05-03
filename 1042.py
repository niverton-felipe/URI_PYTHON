n1, n2, n3 = list(map(int, input().split()))

maior = 0
intermediario = 0
menor = 0

if (n1 < n2) and (n1 < n3):
    menor = n1 
elif(n2 < n3) and (n2 < n1):
    menor = n2
else:
    menor = n3

if (n1 > n2) and (n1 > n3):
    maior = n1 
elif(n2 > n1) and (n2 > n3):
    maior = n2
else:
    maior = n3

if n1 != maior and n1 != menor:
    intermediario = n1
elif n2 != maior and n2 != menor:
    intermediario = n2
else:
    intermediario = n3

print(menor)
print(intermediario)
print(maior)
print()
print(n1)
print(n2)
print(n3)