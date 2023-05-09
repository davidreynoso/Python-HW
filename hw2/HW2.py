# HW2
# Name:
# Collaborators:
# Date:

import random

def count_characters(s):
    """Count the number of occurrences of each character in a string. 
    Args:
        s: str, the string in which to count. 
    Returns:
        a dict keyed by characters whose values are the number of occurrences in s
    """
    my_dict = dict()
    # loop through s, utilizing an if statement to add any new items from s to the dict, 
    # and to add an occurence to items from s already in the dict
    for i in s:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    return my_dict


def count_ngrams(s, n):
    """Count the number of occurrences of n-grams in a string. 
    Args:
        s: str.
        n: positive int. should have default value 1.
    Returns:
        a dict keyed by n-grams whose values are the number of occurrences in s
    """
    my_dict = dict()
    #using the indexs of s to pick out sequential substrings of length n to add to our dict
    # if we already have added that n gram, we add 1 to the occurence
    for i in range(len(s)):
        if (s[i:i+n] in my_dict) and (len(s[i:i+n]) == n):
            my_dict[s[i:i+n]] += 1
        elif len(s[i:i+n]) == n:
            my_dict[s[i:i+n]] = 1
    return my_dict


def markov_text(s, n = 1, length = 100, seed = "I am temporary"):
    """Generate fake text according to an n-th order Markov model, with data from a user-supplied corpus. 
    Args:
        s: str. the text from which to learn grams.
        n: positive int. the order of the Markov model. 
        length: positive int. the number of synthetic characters to generate. should have a default value. 
        seed: str. should have a default value.
    Returns:
        The output string fake_text. fake_text starts with the seed. 
        length of fake_text = length of seed + argument 'length'
    """
    my_dict = count_ngrams(s, n+1)
    # create list of all the options, weights from our dict to make it easier to make lists of 
    # the specific options and weights we need for the next letter
    tot_options = list(my_dict.keys())
    tot_weights = list(my_dict.values())
    # our default seed will pick a random word from the total options we took from the dict,
    # this will be correct length by construction
    if seed == "I am temporary":
        seed = random.choice(tot_options)
    # fake text begins with the seed
    fake_text = seed
    options = list()
    weights = list()
    # while loop makes sure the fake_text is the correct length
    while (len(fake_text) < (len(seed) + length)):
        # we loop through total options to find the options that match the most recent text
        # and puts it into the list, also making a list adding its associated weight (same index)
        for i in range(len(tot_options)):
            if (tot_options[i])[:n] == fake_text[-n:]:
                options.append(tot_options[i])
                weights.append(tot_weights[i])
        # takes a random option based on weights and uses its last letter to continue the fake text
        fake_text += ((random.choices(options,weights))[0])[-1]
        options = []
        weights = []
    return fake_text
            
    