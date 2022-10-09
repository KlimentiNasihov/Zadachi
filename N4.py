def my_dict(a, s, d):
    a = {'a':500, 'b':5874, 'c':560, 'd':400, 'e':5874, 'f':20}
    s = a.values()
    d = []
    for value in s:
         d.append(max(s))
         del a[max(a, key=lambda k: a[k])]
         d.append(max(s))
         del a[max(a, key=lambda k: a[k])]
         d.append(max(s))
         del a[max(a, key=lambda k: a[k])]
         return d
a = {'a':500, 'b':5874, 'c':560, 'd':400, 'e':5874, 'f':20}
s = (a.values())
d = []
print(my_dict(a, s, d))