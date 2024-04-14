A = int(input())
LIST = []

while True:
    if A in range(1, 10):  
        LIST.append(A) 
        break  
    else:
        print("1~9까지의 수만 입력해주세요.")
        A = int(input())  

B = int(input())  

RESULT = LIST[0] * 10 + B  
print(RESULT)
