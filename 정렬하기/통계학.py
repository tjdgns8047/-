import sys; l=[]
n=int(sys.stdin.readline()[:-1])
for i in range(n):
    l.append(int(sys.stdin.readline()[:-1]))
# l.sort()
print(int(sum(l)/n))#산술평균
print(l[int(n/2)])#중 앙 값
print(max(set(l), key=l.count))
print(max(l)-min(l))#범 위
# print(l[1])#최빈값


