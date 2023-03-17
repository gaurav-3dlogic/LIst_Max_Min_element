#Find maximum element in list

n = [5,8,4,1,25,6,3]


max1 = n[0]

for i in n:
    if i > max1:
        max1 = i
print(max1)