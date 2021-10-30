def generateKunciDekripsi(p,q,e):
    n = p * q
    theta = (p-1)*(q-1)
    d = 0
    for k in range (1000):
        d = (1 + k*theta) / e

        if (d == round(d,0)):
            break
    return d

# generateKunciDekripsi(47,71,79)

def olahPesanFromKalimat(pesan):
    pesan = pesan.strip()
    split_strings = [pesan[index : index + 4] for index in range(0, len(pesan), 4)]
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
        if (len(temp) != (4/2)):
            res.append(str(temp[2]+temp[3]))
    return res

# print(olahPesanFromKalimat('HELLOALICE'))

def olahPesanToKalimat(array):
    res = []
    for i in range (len(array)):
        res.append(chr(int(array[i][:2])+97))
        res.append(chr(int(array[i][2:])+97))
    return res
def encryptRSA(pesan,p,q,e):
    m_array = []
    n = p * q
    for i in range (len(pesan)):
        temp = pow(int(pesan[i]), int(e) ,int(n))
        if (temp < 1000):
            temp2 = "0"+str(temp)
            m_array.append(temp2)
        else:
            m_array.append(str(temp))
    return(m_array)

def decryptRSA(ciphertext,p,q,d):
    m_array = []
    n = p * q
    for i in range (len(ciphertext)):
        temp = pow(int(ciphertext[i]), int(d), int(n))
        if (temp < 1000):
            temp2 = "0"+str(temp)
            m_array.append(temp2)
        else:
            m_array.append(str(temp))
    return(m_array)

temp = encryptRSA(olahPesanFromKalimat('HELLOALICE'),47,71,79)
listToStr = ' '.join([str(elem) for elem in temp])
temp2 = olahPesanToKalimat(decryptRSA(encryptRSA(olahPesanFromKalimat('HELLOALICE'),47,71,79),47,71,generateKunciDekripsi(47,71,79)))
listToStr2 = ''.join([str(elem) for elem in temp2])
print(listToStr)
print(listToStr2)
# print(listToStr)
# olahPesanToKalimat(olahPesanFromKalimat('HELLOALICE'))

# print(decryptRSA(encryptRSA(olahPesanFromKalimat('HELLOALICE'),47,71,79),47,71,generateKunciDekripsi(47,71,79)))