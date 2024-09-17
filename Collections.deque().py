from collections import deque
d = deque()
N = int(input())

for _ in range(N):
    A = list(input().split())
    operation = A[0]
    
    if len(A) > 1:
        getattr(d, operation)(A[1])
    else:
        getattr(d, operation)()

for i in d:
    print(i, end=' ')
