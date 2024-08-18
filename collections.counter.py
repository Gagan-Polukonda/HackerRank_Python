from collections import Counter

X = int(input())
shoe_sizes = Counter(list(map(int, input().split())))
N = int(input())

total = 0
for _ in range(N):
    l = list(map(int, input().split()))
    if (l[0] in shoe_sizes.keys()) and shoe_sizes[l[0]]>0:
        total += l[1]
        shoe_sizes[l[0]] -= 1

print(total)