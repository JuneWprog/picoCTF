nums=[16,9,3,15,3,20,6,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14]

flag=''
#uppercase A =1 , ascii 'A' =65

for n in nums:
    flag += chr(n+64)
print(flag)

