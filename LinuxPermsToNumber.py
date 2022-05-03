def perm_to_num(symbolic):
    perms = {'---': '0','--x': '1','-w-': '2','-wx': '3','r--': '4','r-x': '5','rw-': '6','rwx': '7'}

    if len(symbolic) == 10: symbolic = symbolic[1:]
    x = (symbolic[:-6], symbolic[3:-3], symbolic[6:])
    return perms[x[0]] + perms[x[1]] + perms[x[2]]

for i in range(int(input())):
    print(perm_to_num(input()))

