def encipher(p, k):
    c = ''
    n = len(k)
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32: a = 64
        b = ord(k[i%n]) - 64
        t = a + b
        if t > 90: t -= 27
        if t == 64: t = 32
        c += chr(t)
    return c

def decrypt(c, k):
    p = ''
    n = len(k)
    for i in range(len(c)):
        a = ord(c[i])
        if a == 32: a = 64
        b = ord(k[i%n]) - 64
        t = a - b
        if t < 65: t += 27
        if t == 91: t = 32
        p += chr(t)
    return p

print('비즈네르 방식')
plainText = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
K = 'ABC'
print('plain Text : ', plainText)
cipherText = encipher(plainText, K)
print('encrypted Text : ', cipherText)
decryptedText = decrypt(cipherText, K)
print('decrypted Text : %s'%(decryptedText))



plainText = 'SAVE PRIVATE RYAN'
print('plain Text : ', plainText)
cipherText = encipher(plainText, K)
print('encrypted Text : ', cipherText)
decryptedText = decrypt(cipherText, K)
print('decrypted Text : %s'%(decryptedText))


    
