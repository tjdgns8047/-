def binomial(n, k):
    if k == n or k ==0:                         #n == k 일때 헷갈림..
        return 1
    return binomial(n-1, k-1) + binomial(n-1, k)

n,k = input().split()
n = int(n)
k = int(k)
print(binomial(n,k))
