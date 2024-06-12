N = int(input())  

for i in range(N):
    K = input()  
    mynum = int(K[-1])  
    if mynum % 2 == 0:  
        print("even")
    else:
        print("odd") 
