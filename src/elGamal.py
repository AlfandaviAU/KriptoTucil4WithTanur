# EL_GAMAL
# 1. Bilangan prima, p (tidak rahasia)
# 2. Bilangan acak, g ( g < p) (tidak rahasia)
# 3. Bilangan acak, x (x < p) (rahasia, kunci privat)
# 4. y = g
# x mod p (tidak rahasia, kunci publik)
# 5. m (plainteks) (rahasia)
# 6. a dan b (cipherteks) (tidak rahasia)

# pilih p
# pilih g dan x
# dengan syarat g < p dan 1 <= x <= p-2
# y = g^x mod p

# Hasil dari algoritma ini:
# - Kunci publik: tripel (y, g, p)
# - Kunci privat: pasangan (x, p)

# proses enkripsi
# susun pesan jadi blok, setiap pesan kurang dari p-1
# pilih k, 1 <= k <= p-2
# a = g^k mod p
# b = y^k m mod p

# proses dekripsi
# pakai x, (a^x)^-1 = a^(p-1-x) mod p
# m = b/(a^x) mod p

p = 2357
g = 2
x = 1751
m = 2035
k = 1520

def bangkitKunciElGamal(p,g,x):
    y = pow(g,x,p)
    key = {
        "public":[y,g,p],
        "private":[x,p]
    }
    return key

# print(bangkitKunciElGamal(p,g,x)["private"])

def enkripsiElGamal(keyPublic,m,k):
    p = keyPublic[2]
    g = keyPublic[1]
    y = keyPublic[0]
    if (0 <= m and m <= p-1):
        if ( 0 <= k and k <= p-1):
            a = pow(g,k,p)
            b = y ** k * m % p
    return a,b

kunci = bangkitKunciElGamal(p,g,x)
ciphertext = enkripsiElGamal(kunci["public"],m,k)

def dekripsiElGamal(ciphertext,keyPrivate):
    a = ciphertext[0]
    b = ciphertext[1]
    # untuk 1/a^x
    seperAx = pow(a,(p-1-x),p)
    m = b * seperAx % p
    return m

print(dekripsiElGamal(ciphertext,kunci["private"]))