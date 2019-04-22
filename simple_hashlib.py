def checkio(hashed_string, algorithm):
    from math import floor, sin
    from operator import neg, lshift
    

    def little_endian(var, arr):
        result = []
        for letter in var:
            result.append(arr[int(letter, 16)])
        return int(''.join(result), 2)
    
    #convert string to hex byte string
    tmp = []
    for letter in hashed_string:
        tmp.append(f'0{ord(letter):b}')
    hashed_string = ''.join(tmp)
    
    # find hash
    if algorithm == 'md5':
        # constants
        a0 = '67452301'
        b0 = 'efcdab89'
        c0 = '98badcfe'
        d0 = '10325476'
        s = [7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22, 5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20, 4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23, 6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21]
        K = []
        for i in range(64):
            K.append(floor(2**32 * abs(sin(i + 1))))
        
        #1
        tmp = hashed_string
        tmp += '1'
        l = 448 - len(tmp) % 512 % 448
        tmp += '0'*l
        
        #2
        l = f'{len(hashed_string):b}'
        l = (64 - len(l))*'0' + l
        hashed_string = tmp + l[32:] + l[:32]
        
        #3
        while hashed_string:
            tmp = hashed_string[:512]
            hashed_string = hashed_string[512:]
            Mstr = []
            for i in range(32, 513, 32):
                Mstr.append(tmp[i-32:i])
            M = [int(i, 2) for i in Mstr]
            
            A = little_endian(a0, Mstr)
            B = little_endian(b0, Mstr)
            C = little_endian(c0, Mstr)
            D = little_endian(d0, Mstr)
            
            for i in range(64):
                if 0 <= i <= 15:
                    F = (B & C) | ((neg(B)) & D)
                    g = i
                elif 16 <= i <= 31:
                    F = (D & B) | ((neg(D)) & C)
                    g = (5 * i + 1) % 16
                elif 32 <= i <= 47:
                    F = B ^ C ^ D
                    g = (3 * i + 5) % 16
                elif 48 <= i <= 63:
                    F = C ^ (B | (neg(D)))
                    g = (7 * i) % 16
                F = F + A + K[i] + M[g]
                A = D
                D = C
                C = B
                B = B + lshift(F, s[i])
            a0 = hex(int(a0, 16) + A)[2:]
            b0 = hex(int(b0, 16) + B)[2:]
            c0 = hex(int(c0, 16) + C)[2:]
            d0 = hex(int(d0, 16) + D)[2:]
        return a0 + b0 + c0 + d0

            

    elif algorithm == 'sha224':
        pass 

    elif algorithm == 'sha256':
        pass

    elif algorithm == 'sha384':
        pass

    elif algorithm == 'sha512':
        pass

    elif algorithm == 'sha1':
        pass
        

print(checkio('welcome', 'md5'))




'''
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('welcome', 'md5') == '40be4e59b9a2a2b5dffb918c0e86b3d7'
    assert checkio('happy spam', 'sha224') == '6e9dc3e01d57f1598c2b40ce59fc3527e698c77b15d0840ae96a8b5e'
'''
        


