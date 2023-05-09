# PIC 16A HW1
# Name: David Reynoso
# Collaborators:
# Date: 1/15/23

mylist = list()
infinitygo = 1
# since we dont update infinity goes, this while loop 
# allows to ask the user forever until an odd integer is entered
while (infinitygo == 1):  
    x = int(input("Please enter an integer."))
    # adds all entries to the list
    mylist.append(x)
    if (x%2 == 1):
        # this is where an odd integer ends the loop
        break
print(mylist)

