from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    d['A'].append(input())
for j in range(m):
    d['B'].append(input())

for i in d['B']:
    count=1
    found = False
    for j in d['A']:
        if i == j:
            print(count, end=' ')
            found = True
        count+=1
    if not found:
        print(-1, end=' ')
    print('')