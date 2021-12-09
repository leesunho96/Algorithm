def encipher(p, k):
    c = ''
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32: a = 96
        t = a + k
        if 90 < t < 97:
            t += 5
        if t > 122:
            t -= 58
        if t == 96: t = 32
        c += chr(t)

    return c


while(True):
    key = input('키: ')
    if key == '999':
        print('프로그램 종료')
        break
    key = int(key)
    plaintext = input('평문 : ')
    ciphertext = encipher(plaintext, key)
    print("암호문 : ", ciphertext)