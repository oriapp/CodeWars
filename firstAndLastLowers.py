x=""
for i in input():
    if i.upper() != i:
        x+=i
print(f"{x[:1]}-{x[len(x)-1:len(x)]}")
