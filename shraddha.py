#1 Display “My Name Is James” as “My**Name**Is**James” using output formatting of a print() function.
'''star = "**"
name = "my{0}name{0}is{0}james"
print(name.format(star))'''

#2 Write a Python program that prints all the numbers from 0 to 6 except 3 .

'''for i in range(0,7):
    if(i==3):
        continue
    print(i)'''

    

#3
'''list1 = ["I ","Pursuing","i","MSC(DSA)"]
list2 = ["am","MBA","n"]'''

#3 Concatenate the above two lists index-wise
'''newlist = list1 + list2
print(newlist)'''

#3b  Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order.

'''for x, y in zip(list1, list2[::-1]):
    print(x,y)'''


#4 (i) Copy element 44 and 55 from the following tuple into a new tuple .
#(ii) Counts the number of occurrences of item 66 from the following tuple.


'''tuple = (11, 22, 33, 44, 55, 66, 66)
tuple = list(tuple)
print(tuple)
newtuple = (tuple[4],tuple[5])

print(newtuple)
print(tuple.count(66))'''
#5  
keys = ['One', 'Two', 'Three']
values = [1, 2, 3]
#(i) from above two lists convert it into the dictionary.
#(ii) Check if a value 2 exists in a dictionary.







