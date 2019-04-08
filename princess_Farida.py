def take_notake(mons_coins,i):
    if len(mons_coins)==1:
        return mons_coins[0]
    if len(mons_coins)==2:
        return max(mons_coins)
    return max([mons_coins[i]+take_notake(mons_coins[i+2:],0),take_notake(mons_coins[i+1:],0)])

n = input()
for j in xrange(n):
    m = input()
    if m > 0:
        z = raw_input().split()
        z = [int(i) for i in z]
        mons_coins = z
        init_index = 0
        a = take_notake(mons_coins,0)
        print 'Case '+str(j+1)+': '+str(a)
    else:
        print 'Case '+str(j+1)+': ' +str(0)

