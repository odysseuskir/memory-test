'''
Author: Odysseus-Abraham Kirikopoulos
License: GNU General Public License v3.0
Version: 1.0 dev
'''

from random_word import RandomWords

rounds = 0

results_1 = 0
results_2 = 0
results_3 = 0
results_4 = 0

while rounds < 5:

    word1 = RandomWords()
    word2 = RandomWords()
    word3 = RandomWords()
    word4 = RandomWords()
    word5 = RandomWords()
    word6 = RandomWords()
    word7 = RandomWords()
    word8 = RandomWords()
    word9 = RandomWords()
    word10 = RandomWords()
    word11 = RandomWords()
    word12 = RandomWords()
    word13 = RandomWords()
    word14 = RandomWords()
    word15 = RandomWords()

    words = [word1.get_random_word(), word2.get_random_word(), word3.get_random_word(), word4.get_random_word(), word5.get_random_word(), word6.get_random_word(), word7.get_random_word(), word8.get_random_word(), word9.get_random_word(), word10.get_random_word(), word11.get_random_word(), word12.get_random_word(), word13.get_random_word(), word14.get_random_word(), word15.get_random_word()]

    print(words)

    rounds += 1

    if round == 1:
        results_1 = input("How many numbers did the user get right?\n")

    elif round == 2:
        results_2 = input("How many numbers did the user get right?\n")

    elif round == 3:
        results_3 = input("How many numbers did the user get right?\n")

    elif round == 4:
        results_4 = input("How many numbers did the user get right?\n")

avg_result = (results_1 + results_2 + results_3 + results_4) / 4
highest_result = max(results_1, results_2, results_3, results_4)

print("The average result is: " + str(avg_result))
print("The highest result is: " + str(highest_result))