let = input().lower()
xs = []
x = dict((i, let.count(i)) for i in let)
for i in x.keys():
    if i != " ": xs.append(f"{i}:{x[i]}")
print(" ".join(xs))
