# Short mode
n = int(input())
r = []
for i in range(n): r.append(int(i) for i in input().split(" "))

st = sorted(r)
x = sum(([x for x in range(st[0], st[-1]+1) if x not in r])) # calculate the sum of missing numbers
if (1 <= n <= 6):
    print(x)