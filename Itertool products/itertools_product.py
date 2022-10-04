from itertools import product
l1=[eval(i) for i in (input().split(' '))]
l2=[eval(i) for i in (input().split(' '))]
l3 = list(product(l1,l2))
for i in l3:
    print(i, end=" ")
