# -*- coding:utf-8 -*-

# please type the word: these
# please type the result: theS-
# You left 5 time(s) guessing!
# ['heist']

def feedback(times=None):
    # Words_ = [K.lower() for K in words.words() if len(K) == 5]
    with open('words_alpha.txt', 'r') as txt:
        txt_ = txt.read().splitlines()
        Words_ = [K.lower() for K in txt_ if len(K) == 5]
    while times < 6:
        times += 1
        print("You left {} time(s) guessing !".format(7 - times))
        word = input("please type the word: ")
        feedback = input("please type the result: ")
        intersection = list(set([k for k in word.lower()]) & set([k for k in feedback.lower()]))
        if word.upper() == feedback:
            print("Good job, see you tomorrow.")
            break
        else:
            for i, c in enumerate(word):
                [Words_.remove(word) for k in Words_ if word in Words_]
                if c.lower() == feedback[i].lower():
                    if feedback[i].isupper():
                        Words_ = [K for K in Words_ if K[i] == c]
                    elif feedback[i].islower():
                        Words_ = [K for K in Words_ if c in K and K[i] != c]
                else:
                    if feedback[i] == "-":
                        Words_ = [K for K in Words_ if c in intersection or c not in K]
            print(Words_)
    print("Oops, see you tomorrow.")

feedback(0)