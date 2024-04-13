H, M, S = map(int, input().split())  
D = int(input())  

TIMESUM = H * 3600 + M * 60 + S

TIMESUM += D

PRINT_H = (TIMESUM // 3600) % 24  
PRINT_M = (TIMESUM // 60) % 60    
PRINT_S = TIMESUM % 60            

print(PRINT_H,PRINT_M, PRINT_S )
