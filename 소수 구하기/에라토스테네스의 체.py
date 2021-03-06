# https://stackoverflow.com/questions/6687296/python-sieve-of-eratosthenes-compact-python
def pgen(n): # Sieve of Eratosthenes generator by Dan Salmonsen
    yield 2
    np = set()
    for q in range(3, n+1, 2):
        if q not in np:
            yield q
            np.update(range(q*q, n+1, q+q)) 

M, N = map(int, input().split())
l=[value for value in list(pgen(N)) if value >= M]
for i in l: print(i)
