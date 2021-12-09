def encipher(p, k):
    c = ''
    for i in range(len(p)):
        t = ord(p[i])
        if t == 32: t = 0
        else: t -= 64
        c += k[t]

    return c

def decrypter(c,k):
    p = ''
    key = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(c)):
        t = ord(c[i])
        if t == 0: t = 32
        else: t -= 64
        p += chr(t)
    return c
plainText = 'SAVE PRIVATE RYAN'
K = 'QHCBEJKARWSTUVD IOPXZFGLMNY'

print('plainText : %s'%(plainText))
encryptText = encipher(plainText, K)
print('encrypted Text: %s'%(encryptText))
decryptText = decrypter(encryptText, K)
print('decrypted Text: %s'%(decryptText))
