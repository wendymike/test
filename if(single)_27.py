count = int(raw_input('input your number: '))
print count
if count >= 90:
    print 'Grade:A'
else:
    if count >= 80:
        print 'Grade:B'
    else:
        if count >= 70:
            print 'Grade:C'
        else:
            if count >= 60:
                print 'Grade:D'
            else:
                print 'Fail'
print 'End'

sex = raw_input('input your sex: ')
if sex == 'male':
    print 'man'
else:
    if sex == 'female':
        print 'woman'
    else:
        print 'error'
