'''
Author: Odysseus-Abraham Kirikopoulos
License: GNU General Public License v3.0
Version: 1.0 Stable
'''

from random import randint

food = ['apple', 'banana', 'pasta', 'pancake', 'ice cream', 'water', 'tea', 'marmelade', 'honey', 'meat', 'cod', 'nuts', 'onion', 'potato', 'toast']
objects = ['ball', 'sign', 'fence', 'chimney', 'car', 'phone', 'trafic lights', 'tv', 'cable', 'earphones', 'desk', 'couch', 'radio', 'computer', 'table']
clothes = ['scarf', 'gloves', 'shoes', 'shirt', 'jeans', 'trousers', 'flip-flops', 'shockes', 'mask', 'bag', 'jacket', 'clock', 'pijama', 'hat', 'belt']
places = ['house', 'church', 'coffee shop', 'barber shop', 'office', 'hospital', 'college', 'school', 'airport', 'city', 'groccery store', 'hotel', 'cinema', 'police  station', 'gas station']
others = ['hemlet', 'name', 'poster', 'swimming', 'route', 'map', 'tree', 'bush', 'language', 'motorcycle', 'bike', 'glass', 'gogles', 'eraser', 'book']

i = randint(0, 14)
word1 = food[i]
i = randint(0, 14)
word2 = objects[i]
i = randint(0, 14)
word3 = clothes[i]
i = randint(0, 14)
word4 = places[i]
i = randint(0, 14)
word5 = others[i]
i = randint(0, 14)
word6 = food[i]
i = randint(0, 14)
word7 = objects[i]
i = randint(0, 14)
word8 = clothes[i]
i = randint(0, 14)
word9 = places[i]
i = randint(0, 14)
word10 = others[i]
i = randint(0, 14)
word11 = food[i]
i = randint(0, 14)
word12 = objects[i]
i = randint(0, 14)
word13 = clothes[i]
i = randint(0, 14)
word14 = places[i]
i = randint(0, 14)
word15 = others[i]

words = [word1, word2, word3, word4, word5, word6, word7, word8, word9, word10, word11, word12, word13, word14, word15]

rounds = 0 # The number of rounds the user will play (max 4)

results = [0, 0, 0, 0] # The number of words the user guessed correctly each round
results_1 = 0 # The number of words the user guessed correctly
results_2 = 0
results_3 = 0
results_4 = 0

instructions = '''
This game will test your memory.
You will be shown 15 random words.
You will tell them to your friend.
Your friend will then have to repeat as many words as he can remember.
You will then have to type how many words they remembered.
You will repeat the process 3 more times (4 in total), using the same 15 words.
Good luck!
\n
'''

gnu_license = '''
Memory tester Copyright (C) 2022 Odysseus-Abraham Kirikopoulos
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.
\n
'''

startup = '''
Author: Odysseus-Abraham Kirikopoulos
License: GNU General Public License v3.0
Version: 1.0 Stable
\n
'''

print(gnu_license + instructions + startup) # Printing startup messages

while rounds <= 4: # The game loop

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