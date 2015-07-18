s1 = 'sonjasper.com'
i = 1
for characters in s1:
    print format(i, '2d'), characters
    i = i + 1
else:
    print 'over'

li1 = [1, 2, 53, 'x', 11]
i = 1
for val in li1:
    print format(i, '2d'), val
    i = i + 1
else:
    print 'over'

li2 = list(s1)
print li2
i = 1
for val in li2:
    print format(i, '2d'), val
    i = i + 1
else:
    print 'over'

i = 1
for val in range(1, 30):
    print format(i, '2d'), val
    i = i + 1
else:
    print 'over'

tup = (1, 2, 3, 4, 5)
for t in tup:
    print t
else:
    print 'over'

print 'readline'
for cc in open('for_27.py', 'r').readline():
    print cc
else:
    print 'over'

li3 = open('for_27.py', 'r').readlines()
print 'readlines'
for cc in open('for_27.py', 'r').readlines():
    print cc
else:
    print 'over'
print len(li3)

for aa in open('for_27.py', 'r').readlines():
    open('temp.txt', 'a+').write(aa)
else:
    print 'over'
