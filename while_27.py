i = 90
while True:
    print i, 'hello'
    i = i + 1
    if i == 100:
        break
else:
    print 'over'
print 'end'

a = 1
s = 0
while a <= 100:
    print s, '+', a, '=', s+a
    s = a + s
    a = a + 1
else:
    print s
print 'end'
