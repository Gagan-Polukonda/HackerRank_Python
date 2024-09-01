from collections import OrderedDict

N = int(input())
Consumers = OrderedDict()

for _ in range(N):
    a, b = input().rsplit(maxsplit=1)
    Consumers.setdefault(a, []).append(int(b))

sum_dict = {key: sum(values) for key, values in Consumers.items()}

for i in sum_dict:
    print(i, sum_dict[i])