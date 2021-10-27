def generateKunciRSA(p,q,e):
    n = p * q
    theta = (p-1)*(q-1)
    d = 0
    for k in range (1000):
        d = (1 + k*theta) / e

        if (d == round(d,0)):
            break
    print(d)


generateKunciRSA(47,71,79)

def olahPesan(pesan,n):
    pesan = pesan.strip()
    split_strings = [pesan[index : index + n] for index in range(0, len(pesan), n)]
    res = []
    for i in range (len(split_strings)):
        temp = []
        for j in range (len(split_strings[i])):
            temp2 = (ord(split_strings[i][j].lower())-97)
            if (temp2 < 10):
                temp3 = "0"+str(temp2)
                temp.append(temp3)
            else:
                temp.append(str(temp2))
        res.append(str(temp[0]+temp[1]))
        if (len(temp) != (n/2)):
            res.append(str(temp[2]+temp[3]))
    return res

print(olahPesan('HELLOALICE',4))
