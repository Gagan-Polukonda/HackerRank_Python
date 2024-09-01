from collections import namedtuple

N = int(input())
Students = namedtuple('Marksheet', input().split())

total = 0
for _ in range(N):
    Ind = Students(*(list(input().split())))
    total += int(Ind.MARKS)

print("%.2f" % (total / N))