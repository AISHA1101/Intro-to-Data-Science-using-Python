from collections import Counter

lst1 = [1,2,3,4]
lst2 = ['a','b','c','d']
z = list(zip(lst1,lst2))
print(z)
l1 = []
l2 = []
l1,l2 = zip(*z)
#res = [l1.append(i),l2.append(j) for i,j in z]
print(list(l1),list(l2))

print(list(enumerate(lst1)))
'''
x = [2,1,5,3,4,4,3,2]
y = Counter(x)
print(y)

l1 = [1,2,3]
l2 = [4,5]
l1.extend(l2)
print(l1)

l1 = [(1,2),(3,4)]
l1[0] = (5,6)
print(l1[0])
'''