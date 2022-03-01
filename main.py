# -*- coding:utf-8 -*-

# import nltk
# nltk.download('words')
from nltk.corpus import words
# dynamic list

words_ = [K.lower() for K in words.words() if len(K) == 5]
reserved = []
unreserved = []
def feedback(times=None):
    global words_, reserved, unreserved
    while times < 7:
        times += 1
        print("You left {} time(s) guessing !".format(7 - times))
        word = input("please type the word: ")
        feedback = input("please type the result: ")
        if word.upper() == feedback.upper():
            print("Good job, see you tomorrow.")
            break
        else:
            for i, c in enumerate(word):
                [words_.remove(word) for k in words_ if word in words_]
                if c.lower() == feedback[i].lower():
                    words_ = [K for K in words_ if c in K]
                    if feedback[i].isupper():
                        reserved.append(feedback[i].lower())
                        print("28 c:", c)
                        words_ = [K for K in words_ if K[i] == c]
                    elif feedback[i].islower():
                        print("30: ", feedback[i])
                        reserved.append(feedback[i])
                        print("32 reserved: ", reserved)
                        words_ = [K for K in words_ if c in K and K[i] != c]
                else:
                    if feedback[i] == "-":
                        unreserved.append(c)
                        intersection = list(set(unreserved) & set(reserved))
                        print("40 intersection: ", intersection)
                        print("41 unreserved: ", unreserved)
                        words_ = [K for K in words_ if c in reserved or c not in K]
                        continue
            print(words_)
feedback(0)