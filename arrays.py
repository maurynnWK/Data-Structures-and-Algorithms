#importing array module with its alias  arr
'''Python has no built in array data structure instead uses the modern list instead
To use arrays in python then i must create an instace of array class from array module'''

import array as arr
my_array1=arr.array('i',[5,8,2,5,9,16,23,30])

my_array2=arr.array('i',[5,8,2,5,9,16,23,30])
# print(my_array1)
# print(my_array2)

my_strarray=arr.array('u',['A','B','C'])
# print(my_strarray)

'''Dealing with insertion operation on an array'''
#At the end of array
my_array1.append(40)
#print(my_array1)

#At the front of the array
my_array1.insert(0,4)


#In between
my_array1.insert(4,100)
print(my_array1)

'''Concatenation or joining of arrays'''
my_strarray=arr.array('u',['A','B','C'])
my_strarray2=arr.array('u',['D','E','C'])

my_new=my_strarray+my_strarray2
print(my_new)


'''Array Traversal'''

#function to traverse and print values in an array passe
def tranverse_array(my_array:arr.array):
    for element in my_array:
        print(element)
# tranverse_array(my_new)

#function to access a single item
def access_by_index(my_array:arr.array,index:int):
  assert index >=0 and index < len(my_array), "Index out of range ,No location index specified"
  print(my_array[index])

# print(my_array1[6])
# access_by_index(my_array1, 6)

'''ArraySearch'''
print(my_array1.index(9))

def search_value(an_array,value):
    for i in an_array:
        if i == value:
            return f"{i} is at index {an_array.index(i)}"
    else:         
       return f"{value} does not exist in the array"
print(search_value(my_array1,200))

'''Array Updation''' 
print(my_array1)   
my_array1[6]=12
my_array1[3]=2

print(my_array1.index(12))

'''Array Deletion'''
my_array1.remove(12)
print(my_array1)
my_array1.pop()
print(my_array1)
my_array1.pop(4)
print(my_array1)