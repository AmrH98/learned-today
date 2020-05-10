def mergecount(b,c):
    d, count = [] , 0
    while len(b) > 0 or len(c) > 0:
        if len(b) > 0 and len(c) > 0:
            if b[0] < c[0]:
                d.append(b[0])
                b = b[1:]
            else:
                d.append(c[0])
                c = c[1:]
                count += len(b)
        elif len(b) > 0:
            d.append(b[0])
            b = b[1:]
        elif len(c) > 0:
            d.append(c[0])
            c = c[1:]
    return d, count

def sortcount(a):
    n = len(a)
    if n <= 1:
     return a, 0
    n = int(n/2)
    b,x = sortcount(a[:n])
    c,y = sortcount(a[n:])
    d,z = mergecount(b,c)
    return d, x+y+z


print ("\n\nFinal run=")
f = open('/Users/amr/Downloads/Coursera/Stanford/Algorithms/Week 2/Test.txt', 'r')
content_array = []
temp = f.read().split('\n')

print(sortcount(temp))
