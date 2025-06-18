n = int(input())
l = []
for i in range(n):
    l.append(input())
print(l)
s = []
k = input()
for i in l:
    if k in i:
        s.append(i)
print(s)