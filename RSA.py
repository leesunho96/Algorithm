def encipher(p, n, pk):
    c = ''
    i = 0
    while i < len(p):
        m = ''
        for j in range(4):
            m += p[i+j]
        i += 4
        a = int(m)
        t = a
        b = 0
        for k in range(pk):
            b = t % n
            t = a*b
        if b < 10:
            c += '000' + str(b)
        elif b < 100:
            c += '00' + str(b)
        elif b < 1000:
            c += '0' + str(b)
        else:
            c += str(b)

    return c


    c = ''
    i = 0
    while i < len(p):
        m = ''
        for j in range(4):
            m += p[i+j]
        i += 4
        a = int(m)
        t = a
        b = 0
        for k in range(sk):
            b = t % n
            t = a*b
        if b < 10:
            c += '000' + str(b)
        elif b < 100:
            c += '00' + str(b)
        elif b < 1000:
            c += '0' + str(b)
        else:
            c += str(b)

    return c
def encode(p):
    m = ''
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32:
            a = 64
        a -= 64
        if a == 0:
            m += '00'
        elif a < 10:
            m += '0' + str(a)
        else:
            m += str(a)
    return m

def decode(p):
    m = ''
    for i in range(0, len(p), 2):
        a = int(p[i:i+2]) + 64
        if a == 64:
            a = 32
        m += chr(a)
    return m

print('RSA')
N = 3713
S = 97
P = 37

plain_text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('plain Text : %s'%(plain_text))
plain_message = encode(plain_text)
print("encoded text: %s"%(plain_message))
cipher_messagciphe = encipher(plain_message, N, P)
print("cipher Text: %s"%(cipher_messagciphe))
plain_messageciphe = encipher(cipher_messagciphe, N, S)
print('decoded text : %s'%(plain_messageciphe))
plain_text = decode(plain_messageciphe)
print("plain text : %s"%(plain_text))


plain_text = "SAVE PRIVATE RYAN "
print('plain Text : %s'%(plain_text))
plain_message = encode(plain_text)
print("encoded text: %s"%(plain_message))
cipher_messagciphe = encipher(plain_message, N, P)
print("cipher Text: %s"%(cipher_messagciphe))
plain_messageciphe = encipher(cipher_messagciphe, N, S)
print('decoded text : %s'%(plain_messageciphe))
plain_text = decode(plain_messageciphe)
print("plain text : %s"%(plain_text))
