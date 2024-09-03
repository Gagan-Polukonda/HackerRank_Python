from collections import Counter

N = int(input())
samples = []

for _ in range(N):
    samples.append(input())
diction = Counter(samples)

print(len(diction))
for i in diction.keys():
    print(diction[i], end=' ')