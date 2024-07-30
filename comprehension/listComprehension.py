#Basic comprehension to add 2 with each element in the list

list = [1,2,3,4,5]
plustwolist  = [n+2 for n in list]
print(plustwolist)

squarelist = [n**2 for n in list]
print(squarelist)

#Comprehension with condition
#Plus 2 only for even numbers
evenplustwolist = [n+2 for n in list if n%2==0]
print(evenplustwolist)

squareoddlist = [n**2 for n in list if n%2 != 0]
print(squareoddlist)