# -*- coding:utf-8 -*-

def feedback(guess_attempts=None):
    with open('words_alpha.txt', 'r') as file:
        word_list = file.read().splitlines()
        candidate_words = [word.lower() for word in word_list if len(word) == 5]
    
    while guess_attempts < 6:
        print("You have {} guess(es) left!".format(6 - guess_attempts))
        guess_attempts += 1
        word = input("Please type the word: ")
        user_feedback = input("Please type the result: ")
        intersection = list(set([char for char in word.lower()]) & set([char for char in user_feedback.lower()]))
        
        if word.upper() == user_feedback:
            print("Good job! See you tomorrow.")
            break
        else:
            for i, char in enumerate(word):
                [candidate_words.remove(word) for candidate_word in candidate_words if word in candidate_words]
                if char.lower() == user_feedback[i].lower():
                    if user_feedback[i].isupper():
                        candidate_words = [candidate_word for candidate_word in candidate_words if candidate_word[i] == char]
                    elif user_feedback[i].islower():
                        candidate_words = [candidate_word for candidate_word in candidate_words if char in candidate_word and candidate_word[i] != char]
                else:
                    if user_feedback[i] == "-":
                        candidate_words = [candidate_word for candidate_word in candidate_words if char in intersection or char not in candidate_word]
            print(candidate_words)

feedback(0)
