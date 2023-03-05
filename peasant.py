def peasant(x, y):    


        first = int(x,16)
        second = int(y,16)
        sum = 0
        while(second > 0):
            if(second & 1): sum = sum^first
            second = second // 2
            first = first * 2
            if(first & 256): first = first^283
        return sum

    

r1 = ['02','03','01','01']
r2 = ['01','02','03','01']
r3 = ['01','01','02','03']
r4 = ['03','01','01','02']

dr1 = ['0e','0b','0d','09']
dr2 = ['09','0e','0b','0d']
dr3 = ['0d','09','0e','0b']
dr4 = ['0b','0d','09','0e']

pt = ['87','6e','46','a6']
ct = ['47','37','94','ed']


def mixCol(pt):

    n1 = hex(peasant(r1[0],pt[0])^peasant(r1[1],pt[1])^peasant(r1[2],pt[2])^peasant(r1[3],pt[3]))
    n2 = hex(peasant(r2[0],pt[0])^peasant(r2[1],pt[1])^peasant(r2[2],pt[2])^peasant(r2[3],pt[3]))
    n3 = hex(peasant(r3[0],pt[0])^peasant(r3[1],pt[1])^peasant(r3[2],pt[2])^peasant(r3[3],pt[3]))
    n4 = hex(peasant(r4[0],pt[0])^peasant(r4[1],pt[1])^peasant(r4[2],pt[2])^peasant(r4[3],pt[3]))
    return n1,n2,n3,n4

def invMixCol(ct):

    n1 = hex(peasant(dr1[0],ct[0])^peasant(dr1[1],ct[1])^peasant(dr1[2],ct[2])^peasant(dr1[3],ct[3]))
    n2 = hex(peasant(dr2[0],ct[0])^peasant(dr2[1],ct[1])^peasant(dr2[2],ct[2])^peasant(dr2[3],ct[3]))
    n3 = hex(peasant(dr3[0],ct[0])^peasant(dr3[1],ct[1])^peasant(dr3[2],ct[2])^peasant(dr3[3],ct[3]))
    n4 = hex(peasant(dr4[0],ct[0])^peasant(dr4[1],ct[1])^peasant(dr4[2],ct[2])^peasant(dr4[3],ct[3]))
    return n1,n2,n3,n4


print(mixCol(pt))
print(invMixCol(ct))
    # fCol = []

        # while 1:
        #     if second%2 == 0:
        #         pass
        #     else: fCol.append(first)

        #     first = first*2
        #     second = second // 2

            
            
        #     if second == 0:
        #         break
        # res = 0
        # for i in fCol:
        #     res = res^i
        # if(res>=256):
        #     return res^283
        # else: return res