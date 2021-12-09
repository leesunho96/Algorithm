def encipher(p, k):
    c = ''
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32: a = 64
        t = a + k
        if t > 90: t -= 27
        if t == 64: t = 32
        c += chr(t)

    return c

def decrypter(c, k):    
    p = ''
    for i in range(len(c)):
        a = ord(c[i])
        if a == 32: a = 64
        t = a - k
        if t < 65: t += 27
        if t == 91: t = 32
        p += chr(t)        
    return p

print('카이사르 방식')
plainText = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
K = 1
print('plain text : %s'%(plainText))
cipherText = encipher(plainText, K)
print('encipher Text : %s'%(cipherText))
decryptText = decrypter(cipherText, K)
print('decrypt Text : %s'%(decryptText))

plainText = 'SAVE PRIVATE RYAN'
print('plain text : %s'%(plainText))
cipherText = encipher(plainText, K)
print('encipher Text : %s'%(cipherText))
decryptText = decrypter(cipherText, K)
print('decrypt Text : %s'%(decryptText))