import math

L = int(input())  
A = int(input())  
B = int(input())  
C = int(input())  
D = int(input()) 

gooka = math.ceil(A / C) 
suhak = math.ceil(B / D)  

breaktime = L - max(gooka, suhak) 

print(breaktime)
