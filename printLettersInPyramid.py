import string
n = int(input())

for i in range(1, n+1):
    print(string.ascii_uppercase[0:i], end="\n")
