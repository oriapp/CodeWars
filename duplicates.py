def narcissistic( x ):
    return len(set(str(x))) == len(str(x))

# OR

def narcissistics( num ):
    return num == sum([int(x) ** len(str(num)) for x in str(num)])