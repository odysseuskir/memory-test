'''
Author: Odysseus-Abraham Kirikopoulos
License: GNU General Public License v3.0
Version: 1.0 Pre Release 1
'''

from random_word import RandomWords # Importing the random word generator

rounds = 0 # The number of rounds the user will play (max 4)

results = [0, 0, 0, 0] # The number of words the user guessed correctly each round
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

instructions = '''
This game will test your memory.
You will be shown 15 random words.
You will tell them to your friend.
Your friend will then tell you the words.
You will then have to type how many words they remembered.
You will repeat the process 3 more times (4 in total), using the same 15 words.
Good luck!
\n
'''

gnu_license = '''
Memory tester Copyright (C) 2022 Odysseus-Abraham Kirikopoulos
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.
\n\n
'''

print(gnu_license + instructions + "Gathering random words... This might take a while...\n") # Printing the license and instructions

words = [word1.get_random_word(), word2.get_random_word(), word3.get_random_word(), word4.get_random_word(), word5.get_random_word(), word6.get_random_word(), word7.get_random_word(), word8.get_random_word(), word9.get_random_word(), word10.get_random_word(), word11.get_random_word(), word12.get_random_word(), word13.get_random_word(), word14.get_random_word(), word15.get_random_word()] # Putting the words in a list

while rounds != 4: # The game loop

    rounds += 1 # Adding 1 to the number of rounds
    print("\nRound " + str(rounds) + " of 4") # Printing the round number
    print(words) # Printing the words

    if rounds == 1:
        results[0] = int(input("\nHow many numbers did the user get right?\n"))  # Asking the user how many words they remembered correctly

    elif rounds == 2:
        results[1] = int(input("\nHow many numbers did the user get right?\n"))

    elif rounds == 3:
        results[2] = int(input("\nHow many numbers did the user get right?\n"))

    elif rounds == 4:
        results[3] = int(input("\nHow many numbers did the user get right?\n"))

avg_result = (results[0] + results[1] + results[2] + results[3]) / 4 # Calculating the average number of words the user guessed correctly
highest_result = max(results[0], results[1], results[2], results[3]) # Calculating the highest number of words the user guessed correctly

print("\nThe average result is: " + str(avg_result)) # Printing the average number of words the user guessed correctly
print("\nThe highest result is: " + str(highest_result)) # Printing the highest number of words the user guessed correctly