# PIC 16A HW1
# Name: David Reynoso
# Collaborators:
# Date: 1/15/23

import random # This is only needed in Problem 5

# Problem 2 

def make_count_dictionary(L):
    ''' Counts how many times each element in a list appears.
    Args:
        L: A list. Elements may be of different types.
    Returns:
        A dict of counts. A key is a unique element of L,
        and its corresponding value is how many times
        that element is in L.
    Example:
        L = ["a", "a", "b", "c"]
        returns {"a" : 2, "b" : 1, "c" : 1}
    '''
    cur_let = ""
    counter = 0
    my_dict = dict()
    for i in range(len(L)):
        # lets us make sure we dont rly to mess with an entered accounted for entry
        if L[i] in my_dict:
            continue
        cur_let = L[i]
        counter += 1
        # iterates list to find the number of occurences
        for j in L[i+1:]:
            if (cur_let == j):
                counter += 1
        # enters into the dict
        my_dict[L[i]] = counter
        counter = 0
    return my_dict
        



# Problem 4

def get_triangular_numbers(k):
    ''' Finds the first k triangular numbers. 
    Args:
        k: A positive integer.  
    Returns:
        A list of the first k triangular numbers,
        in order. Each element is an integer.
    Example:
        k = 6
        returns [1, 3, 6, 10, 15, 21]
    '''
    tri_list = list()
    if (k >= 1):
        tri_list.append(1)
        # utilize range to get numbers 2-k and creates triangle numbers
        # with loop using already appended "1"
        for i in range(2,int(k)+1):
            tri_list.append(i + tri_list[-1])
    return (tri_list)
    


def get_consonants(s):
    ''' Finds only the consonant letters in a string.
    Args:
        s: A string that contains only lowercase alphabet letters,
        vowels, spaces, commas, and periods.
    Returns:
        A list of strings. Each element
            - is one character long,
            - is not a vowel, space, comma, nor period,
            - is in s, and
            - may appear multiple times.
        The elements appear in the same order as the letters in s.
    Example:
        s = "make it so, number one."
        returns ["m", "k", "t", "s", "n", "m", "b", "r", "n"]    
    '''
    con_list = list()
    # iterates and checks if the characters are ones we desire and 
    # we add it to our 'constant list' 
    for i in s:
        if i not in ["a", "e", "i", "o", "u", " ", ",", "."]:
            con_list.append(i)
    return(con_list)
            


def get_list_of_powers(X, k):
    ''' Raise elements of a list to its powers.
    Args:
        X: A list of non-negative integers.
        k: A non-negative integer.
    Returns:
        A list of lists. The ith element is a list
        of the powers of X[i] from 0 to (and including) k, 
        in increasing order.
    Example:
        X = [5,6,7], k = 2
        returns [[1, 5, 25], [1, 6, 36], [1, 7, 49]]
    '''
    pow_list = list()
    for i in range(len(X)):
        # create the list within our list to store powers for a specific number
        pow_list.append(list())
        # adds all the powers to the respective lists created in our pow_list
        for j in range(k+1):
            pow_list[i].append(X[i]**j)
    return (pow_list)


def get_list_of_even_powers(X, k):
    ''' Raise elements of a list to its even powers.
    Args:
        X: A list of non-negative integers.
        k: A non-negative integer. May or may not be even.
    Returns:
        A list of lists. The ith element is a list
        of the EVEN powers of X[i] from 0 to (and including) k, 
        in increasing order.
    Example:
        X = [5,6,7], k = 2
        returns [[1, 25], [1, 36], [1, 49]]
    '''
    epow_list = list()
    for i in range(len(X)):
        epow_list.append(list())
        # since j will be both the index and the power raised to
        # we can see if j is odd and filter for the even powers
        for j in range(k+1):
            if (j%2 == 0):
                epow_list[i].append(X[i]**j)
    return (epow_list)



# Problem 5

def random_walk(ub, lb):
    ''' Simulates a simple, unbiased random walk.
    Terminates when the walk's position reaches
    the upper bound or lower bound. Initial position is 0.

    Args:
        ub: An integer. Upper bound of the walk.
        lb: An integer. Lower bound of the walk.
        You can assume ub >= lb.
    Returns:
        pos: An integer. The walk's final position.
        positions: A list of integers. A log of the walk's positions, 
        including initial but excluding final position.
        steps: A list of -1s and 1s. A log of the coin flips.
    '''
    pos = 0
    # add 0 as at timestep 0 we start here
    positions = [0]
    steps = list()
    Cur_choice = 0
    infin = 0
    # loop that only stops when bound is reached
    while (infin == 0):
        # create a 1 or -1 step randomly
        Cur_choice = random.choice([1,-1])
        # store the random choice in steps list
        steps.append(Cur_choice)
        # update our position
        pos += Cur_choice
        if ((pos == ub) or (pos ==lb)):
            break
        elif ((pos < ub) and (pos > lb)): 
            # appends the updated position to our positions list
            positions.append(pos)
    return pos,positions,steps
