import binascii

def binascii_base16_decoding(base16_string):
    decoded_bytes = binascii.unhexlify(base16_string)
    
    decoded_string = decoded_bytes.decode('utf-8')
    
    return decoded_string

if __name__ == "__main__":
    base16_string = input()
    print(binascii_base16_decoding(base16_string))
