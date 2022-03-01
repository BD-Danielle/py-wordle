# -*- coding:utf-8 -*-

# please type the word: thorn
# please type the result: T-Or-
# Unreserved:  ['h']
# Reserved letter(s):  ['t', 'o', 'r']
# Unreserved letter(s):  ['h', 'n']
# hint(s): ['troad', 'troat', 'troca', 'trock', 'troco', 'trode', 'troft', 'trogs', 'troic', 'troke', 'troll', 'tromp', 'troop', 'troot', 'trope', 'trout', 'trove']

from nltk.corpus import words

Words_ = [K.lower() for K in words.words() if len(K) == 5]
Reserved = []
Unreserved = []

def feedback(times=None):
    global Words_, Reserved, Unreserved
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
                [Words_.remove(word) for k in Words_ if word in Words_]
                if c.lower() == feedback[i].lower():
                    if feedback[i].isupper():
                        Reserved.append(feedback[i].lower())
                        Words_ = [K for K in Words_ if K[i] == c]
                    elif feedback[i].islower():
                        Reserved.append(feedback[i])
                        print("32 Reserved: ", Reserved)
                        Words_ = [K for K in Words_ if c in K and K[i] != c]
                else:
                    if feedback[i] == "-":
                        Unreserved.append(c)
                        # intersection = list(set(Unreserved) & set(Reserved))
                        # print("40 intersection: ", intersection)
                        print("41 Unreserved: ", Unreserved)
                        Words_ = [K for K in Words_ if c in Reserved or c not in K]
            print(Words_)
feedback(0)