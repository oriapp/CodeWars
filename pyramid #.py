
n = int(input())

if 0 < n < 100:
    arr = []
    for i in range(1,2):
        arr.append("#" * n)
        for x in range(1,n - 1):
            arr.append("#" + " " * (n-2) + "#")
        arr.append("#" * n)
    print("\n".join(arr))
else:
    print("#")