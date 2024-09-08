'''
n=int(input())
j=n-1
for i in range(1,n+1):
    print(" "*j,end="")
    print("*"*i,end="")
    if n>=2:
       print("*"*(i-1))
    j-=1
j=0
for i in range(n,0,-1):
    print(" "*j,end="")
    print("*"*i,end="")
    if i>1:
        print("*"*(i-1))
    j+=1
    


n=int(input())
a=0
b=1
print(a,b,end="")
for i in range(n-2):
    z=a+b
    print(z,end="")
    a=b
    b=z
'''


n=int(input())
j=n
m=0
c=len(str(n))
while j>0:
   d=j%10
   if c==0:
        break
   else:   

    m+=d*(10**c)
    c-=1
   
    j=j//10
print(m)
 
'''
n=5
for i in range(1,n+1):
    if i<=n//2:
        for j in range(n-(2*i)+1):
                print(" ",end='')
        for k in range(2*i-1):
            print("*", end=' ')
    
    elif i==n:
         print()
         for i in range(n):
              print('*',end=' ')
'''
