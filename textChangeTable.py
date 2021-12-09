def encipher(p, k):
    c = ''
    for i in range(len(p)):
        t = ord(p[i])
        if t == 32: t = 0
        else: t -= 64
        c += k[t]

    return c

def decrypter(c,k) :
    p=''
    b=0
    x = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(c)):
        a = ord(c[i])
        for j in range(len(k)):
            b = ord(k[j])
            if a == b :
                p+=x[j]
                break
    return p
print('문자변환표')
plainText = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
K = 'QHCBEJKARWSTUVD IOPXZFGLMNY'

print('plainText : %s'%(plainText))
encryptText = encipher(plainText, K)
print('encrypted Text: %s'%(encryptText))
decryptText = decrypter(encryptText, K)
print('decrypted Text: %s'%(decryptText))

plainText = 'SAVE PRIVATE RYAN'
print('plainText : %s'%(plainText))
encryptText = encipher(plainText, K)
print('encrypted Text: %s'%(encryptText))
decryptText = decrypter(encryptText, K)
print('decrypted Text: %s'%(decryptText))
