# doesnt work
def gcd(r0, r1):
    r0 = int(r0, 16)
    r1 = int(r1, 16)

    s0 = 1
    s1 = 0
    i = 1
    t0 = 0
    t1 = 1

    ri = 1

    while r1!=0:
        i+=1
        ri = r0%r1
        qi_1 = (r0-ri)//r1
        si = s0 - (qi_1*s1)
        ti = t0 - (qi_1*t1)

        r0 = r1
        r1 = ri

        s0 = s1
        s1 = si

        t0 = t1
        t1 = ti
    return r1, s1, t1

print(gcd('67','12'))

