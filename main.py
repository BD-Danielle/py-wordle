# -*- coding:utf-8 -*-

# import nltk
# nltk.download('words')
import re
from pickle import TRUE
from nltk.corpus import words

# print(type(words.words()))

# print(len(A)) 236736
# print(words_list)
# dough -> ['-----', ()] -> ('d', 'o', 'u', 'g', 'h') del 1 word del 5 letters 'd', 'o', 'u', 'g', 'h'
# if first input as '-----' del 1 word and 5 letters, no need to ask second input in round 1
# and renew list...
# alias -> ['--i--', ('l', 's')] del 1 letter 'a'
# renew list
# smile -> ['s-il-', ()] del 2 letters 'm', 'e'
# renew list
# still -> ['s-ill', ()] del 1 letter 't'
# renew list
# spill -> ['s-ill', ()] del 1 letter 'p'
# renew list
# swill -> ['swill', ()] del 0 letter
def renewDict(result, bool, letter):
    if bool:
        return result
    else:
        keep = [K for K in result if letter not in K]
        print(keep, len(keep), "words have been kept!!!")
        return keep


def detectLetter(letter, reference, idx=None):
    if letter:
        if idx:
            result = [K for K in reference if letter in K[idx]]
        else:
            result = [K for K in reference if letter in K]
        if result:
            return renewDict(result, True, letter)
        else:
            return renewDict(result, False, letter)

# global A
# global A5
# global words_list
A = words.words()
A5 = [K.lower() for K in A if len(K) == 5]
# dynamic list
words_list = [list(K) for K in A5]
round1 = 0

def prompt(round1=None):
    if not round1:
        print("Wellcome to WORDLE !!!")
        prompt(True)
    else:
        # dynamic list
        global words_list
        while round1 <= 5:
            print("You left {} times guessing !".format(6 - round1))
            round1 += 1
            print("Skip(Enter) if not a word in the correct spot")
            spotA = input()
            if not spotA:
                print("Oops, all the letters are not in any spot.")
                print("Please input correct letters for renewing the Dict")
                spotB = input()
                if spotB:
                    print("We will renew the Dict")
                    for idx, letter in enumerate(list(spotB)):
                        words_list = detectLetter(letter, words_list)
                else:
                    print('Enter(skip) then break')
                # The letters are not in the word in any spot.
                print("Please input incorrect letters for renewing the Dict")
                spotC = input()
                if spotC:
                    for idx, letter in enumerate(list(spotC)):
                        words_list = renewDict(words_list, False, letter)
                    # print(len(words_list))
                    print("Go next round!!!")
                    print("round1: ", round1)
                else:
                    print('Enter(skip) then break')
                    break
            else:
                number = 0
                for idx, letter in enumerate(list(spotA)):
                    if letter != "-":
                        number += 1
                        if(number == 5):
                            break
                        words_list = detectLetter(letter, words_list, idx)
                        print('The letter {} is in the word and in the {}th spot.'.format(letter, idx))
                print(len(words_list))
                print("Please input correct letters for renewing the Dict")
                spotB = input()
                if spotB:
                    print("We will renew the Dict")
                    for idx, letter in enumerate(list(spotB)):
                        words_list = detectLetter(letter, words_list)
                else:
                    print('Enter(skip) then break')
                # The letters are not in the word in any spot.
                print("Please input incorrect letters for renewing the Dict")
                spotC = input()
                if spotC:
                    for idx, letter in enumerate(list(spotC)):
                        words_list = renewDict(words_list, False, letter)
                    # print(len(words_list))
                    print("Go next round!!!")
                    print("round1: ", round1)
                else:
                    print('Enter(skip) then break')
                    break
            # prompt(round1)
    print("Good job")
    


prompt()