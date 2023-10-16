array= [1,3,5,7,9]
array.reverse()

for i in range(len(array)):
    array[i] = array[i] + 1
    
print(array)