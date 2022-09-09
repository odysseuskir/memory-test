'''
Author: Odysseus-Abraham Kirikopoulos
License: GNU General Public License v3.0
Version: 1.1 dev
'''

from random_word import RandomWords # Importing the random word generator

rounds = 0 # The number of rounds the user will play (max 4)

results_1 = 0 # The number of words the user guessed correctly
results_2 = 0
results_3 = 0
results_4 = 0

word1 = RandomWords() # Generating the random words
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

words = [word1.get_random_word(), word2.get_random_word(), word3.get_random_word(), word4.get_random_word(), word5.get_random_word(), word6.get_random_word(), word7.get_random_word(), word8.get_random_word(), word9.get_random_word(), word10.get_random_word(), word11.get_random_word(), word12.get_random_word(), word13.get_random_word(), word14.get_random_word(), word15.get_random_word()] # Putting the words in a list

while rounds < 5: # The game loop

    print(words) # Printing the words

    rounds += 1 # Increasing the number of rounds

    if rounds == 1:
        results_1 = int(input("\nHow many numbers did the user get right?\n"))  # Asking the user how many words they guessed correctly

    elif rounds == 2:
        results_2 = int(input("\nHow many numbers did the user get right?\n"))

    elif rounds == 3:
        results_3 = int(input("\nHow many numbers did the user get right?\n"))

    elif rounds == 4:
        results_4 = int(input("\nHow many numbers did the user get right?\n"))

avg_result = (results_1 + results_2 + results_3 + results_4) / 4 # Calculating the average number of words the user guessed correctly
highest_result = max(results_1, results_2, results_3, results_4) # Calculating the highest number of words the user guessed correctly

print("\nThe average result is: " + str(avg_result)) # Printing the average number of words the user guessed correctly
print("\nThe highest result is: " + str(highest_result)) # Printing the highest number of words the user guessed correctly

#This program is protected under the GNU General Public License v3.0. Odysseus-Abraham Kirikopoulos | 2022 | Some rights reserved.