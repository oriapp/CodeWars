import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
arr = []
for i in range(1, n*10+1):
    arr.append(str(n*i))

print(" ".join(arr[:10]))