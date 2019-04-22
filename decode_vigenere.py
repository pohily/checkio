def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    key, result, d_key = '', '', []
    # find cycled key
    for index, letter in enumerate(old_decrypted):
        d = ord(letter) - ord(old_encrypted[index])
        d_key.append(d)
        if 0 <= d:
            key += chr(65 + d)
        else:
            key += chr(91 + d)
    
    # find key
    for i in range(1, len(key)):
        cycle = (len(key) // len(key[:i]) + 1) * key[:i]
        cycle = cycle[:len(key)]
        if key == cycle:
            key = key[:i]
            break
    d_key = d_key[:len(key)]
    # decrypt
    
    k = len(key)
    for i, v in enumerate(new_encrypted):
        p = ord(v) + d_key[i % k]
        if 65 <= p <= 90:
            result += chr(p)
        elif p < 65:
            result += chr(26 + p)
        elif p > 90:
            result += chr(65 + p % 91)
    return result
print(decode_vigenere("NOBODYEXPECTSTHESPANISHINQUISITION", "PVFQNGSZWIEDAHJLWRKVWUOMPACWUPXKYV", "QBVGHXSTAWFOAQTPFGIWICZEPKXDCSPKXOZAKYNVNSNSSYEVWOHKKXIHKCIVSUWFSEEUQBIPRKXQHKHXKFMGRPRGVMGULEUSTMFVQKXIHGKRQCMBULSHRCAQBVVOLWQBWEYUDCUCCXLWTYIRBMGUPFNILFCIEPNIKHBPCXLKJLVGKAWPTSUDXFQMIUCQCPZXJOASYVYNNJSEVRUSLSTHFNOLFCDFCMSGKUGJKZHGYIFKKQQBRVKVQAALGIIFGHTQCQHKCIDYWB"))    
"""
"""               



