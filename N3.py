def jj(a, b):
    d = list()
    for i in a:
        for s in b:
            if i == s:
                d.append(i)
    return d
a=[1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(jj(a, b))