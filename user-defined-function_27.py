def test_a():
    print 'hello!!!'
    print 'hehehehehehe!'

def test_b(val1, val2):
    print val1,
    print val2

def test_c(n1, n2):
    print n1,
    print n2
    n = n1 + n2
    return n

def test_d(n1, n2):
    print n1,
    print n2
    x = n1 + n2
    m = n1 * n2
    p = n1 - n2
    return x, m, p

def test_e(a, b, c = 5):
    z = a - b - c
    return z

print 'Entry programme'
test_a()
test_b(121211, 'lalalallala')
pls = test_c(100, 200)
print 'sum =', pls
pls, multi, mi = test_d(20, 10)
print pls, multi, mi
re = test_d(20, 10)
print re
print re[0], re[1], re[2]
z = test_e(50, 26)
print 'z =', z
print 'The end'
