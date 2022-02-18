broj,pali,sest,sedam,osam,devet,deset,nije_izaslo,moja_ocena = 0,0,0,0,0,0,0,0,0
podela,a,b,c,r,d,e,m,k = [],[],[],[],[],[],[],[],[]
moj_indeks='2021/0393'
with open('spisak.txt', 'r+') as f:
    for i in f:
        c.append(i[0:len(i) - 1])
        indeks=i[0:9]
        #print(moj_indeks)
        if indeks == moj_indeks:
            moja_ocena=c[-1][-1]
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
print('Moja ocena:',moja_ocena)
print('Procenat palih:',round(pali/broj *100,2),'%')
print('\n5:',pali,'\n6:',sest,'\n7:',sedam,'\n8:',osam,'\n9:',devet,'\n10:',deset)
