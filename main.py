broj = 0
podela = []
pali = 0
sest = 0
sedam = 0
osam = 0
devet = 0
deset = 0
nije_izaslo = 0
c = []
a = []
b = []
r = []
d = []
e = []
m = []
k = []
with open('spisak', 'r+') as f:
    for i in f:
        c.append(i[0:len(i) - 1])

        if (c[-1][-1]) == '5':
            # c=[]
            pali += 1
            a.append(c[-1])
        if (c[-1][-1]) == '6':
            # c=[]
            sest += 1
            b.append(c[-1])

        if (c[-1][-1]) == '7':
            # c=[]
            sedam += 1
            r.append(c[-1])
        if (c[-1][-1]) == '8':
            # c=[]
            osam += 1
            d.append(c[-1])

        if (c[-1][-1]) == '9':
            # c=[]
            devet += 1
            e.append(c[-1])

        if (c[-1][-1]) == 'N':
            nije_izaslo += 1
            k.append(c[-1])
            broj -= 1
        if (c[-1][-1]) == '0':
            # c=[]
            deset += 1
            m.append(c[-1])
        broj += 1

    with open('pali.txt', 'w') as p:
        for i in a:
            p.write(f'{i}\n')
    with open('sest.txt', 'w') as p:
        for i in b:
            p.write(f'{i}\n')
    with open('sedam.txt', 'w') as p:
        for i in r:
            p.write(f'{i}\n')
    with open('osam.txt', 'w') as p:
        for i in d:
            p.write(f'{i}\n')
    with open('devet.txt', 'w') as p:
        for i in e:
            p.write(f'{i}\n')
    with open('nisu izasli.txt', 'w') as p:
        for i in k:
            p.write(f'{i}\n')
    with open('deset.txt', 'w') as p:
        for i in m:
            p.write(f'{i}\n')
print((pali * 5 + 6 * sest + 7 * sedam + 8 * osam + 9 * devet + 10 * deset) / broj)
