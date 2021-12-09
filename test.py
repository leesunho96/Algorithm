def encipher(p,k) :
    c=''
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32 :
            a = 0
        else :
            a-=64
        c+=k[a]
    return c
def decipher(p,k) :
    c=''
    b=0
    x = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(p)):
        a = ord(p[i])
        for j in range(len(k)):
            b = ord(k[j])
            if a == b :
                c+=x[j]
                break
    return c
plainText='SAVE PRIVATE RYAN'
K = 'QHCBEJKARWSTUVD IOPXZFGLMNY'
print('평문 : ',plainText)
print('Key : ',K)
chipherText = encipher(plainText,K)
print('암호문 : ',chipherText)
dhipherText = decipher(chipherText,K)
print('복호문 : ',dhipherText)

plainText=' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print('평문 : ',plainText)
print('Key : ',K)
chipherText = encipher(plainText,K)
print('암호문 : ',chipherText)
dhipherText = decipher(chipherText,K)
print('복호문 : ',dhipherText)