height = int(input())

for i in range(1,height+1):

    for j in range(1, height*2):
    
        if(j <= height-i+1):
            
            print(j,end=" ")
        
        elif(j >= height+i-1):
        
            print(height*2-j,end=" ")
            
        else:
        
            print(end="  ")
            
    
    print()
    
# Sample Input :- 5
# Output :- 
# 1 2 3 4 5 5 4 3 2 1
# 1 2 3 4     4 3 2 1
# 1 2 3         3 2 1
# 1 2             2 1
# 1                 1
