import binascii

def binascii_base64_decoding(base64_string):
    # base64 디코딩 수행
    decoded_bytes = binascii.a2b_base64(base64_string)
    
    # 바이트를 문자열로 디코딩
    decoded_string = decoded_bytes.decode('utf-8')
    
    return decoded_string

if __name__ == "__main__":
    base64_string = input()
    print(binascii_base64_decoding(base64_string))
