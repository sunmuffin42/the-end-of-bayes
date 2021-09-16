"""
1) guess from most common/necessary letters (vowels, <s>, etc)
1a) succeed
1b) fail
2) update possible words in priors based on (1a)'s inclusions and (1b)'s exclusions
repeat
3) assess if likelihood is high enough to be correct, ie play with a ratio of satisfactory probability, so it gets good enough at guessing without too much loss. add parameters: how many possible letters there are unguessed, how many possible words there are with those letters, how many limbs have been drawn
4) assess if it's worth guessing a word or a letter
4a) guess, success
4b) guess, fail, repeat

the likelihood of being correct in a whole word guess may end up saving our ass right?
if we random strings of arbitrary length but kept max loss at 6 (head, torso, four limbs), would that change it?
"""
import random

# assess ratio, return word or letter

# assess remaining possible strings

# 
def executioner_begin():
    dictionary = open("dictionary.txt", mode="r").readlines()

# if multiple

"The End of iCarly"