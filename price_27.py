aipp = raw_input('����ţ�̵�����: ')
ai11 = raw_input('���뼦��������: ')
ai22 = raw_input('�������������: ')
ai33 = raw_input('�����㳦������: ')
aip = int(aipp)
ai1 = int(ai11)
ai2 = int(ai22)
ai3 = int(ai33)

def z(aip ,ai1, ai2, ai3, ap = 20, a1 = 15, a2 = 16, a3 = 6):
    zong = aip * 20 + ai1 * a1 + ai2 * a2 + ai3 * a3
    return zong

zong = z(aip, ai1, ai2, ai3)
print '�ܽ�� =', zong

