'''
You are given a string s and a dictionary of words. 
You need to determine if s can be segmented into a space-separated sequence of dictionary words. 
Design an algorithm using dynamic programming that solves this problem in O(n^2) time complexity and 
O(n) space complexity, where n is the length of the string s.
'''

def segment(string:str, words):
    new_string = ""
    length_of_string = len(string)
    # make a loop na nagloop sa loob ng string
    # make a loop na nagloop sa dictionary
    for every_letter in range(length_of_string):
        for every_word in words:
            every_word_in_words = every_word
            the_letter_in_the_string = string[every_letter: every_letter + len(every_word_in_words)]

            if every_word_in_words == the_letter_in_the_string:
                new_string += every_word + " "
                return True
            else:
                return False

    return new_string
           



dict_of_words = {"slay": True, "queen": True, "yas": True}
s = input("write slayqueenyas pls: ")
print(segment(s, dict_of_words))
# if input = slayqueen
# loop through
# match to the dictionary
# then
# put space in-between
