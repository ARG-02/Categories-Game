import numpy as np
import random
import time
import os

# randomly generates list of 26 letters without replacement
letters = [chr(char) for char in (65 + np.random.choice(26, 26, replace=False))]

# grabs list of categories from file
with open('Categories.txt', 'r') as file:
    categories = file.readlines()

# sets number of categories for game
os.system(f"say How many categories do you want?: ")
NUM_CATEGORIES = input("How many categories do you want?: ")

while type(NUM_CATEGORIES) != int:
    print(NUM_CATEGORIES + "is not a valid number.")
    NUM_CATEGORIES = input("How many categories do you want?: ")

if NUM_CATEGORIES > len(categories):
    print('There are too few provided categories in the text file.')
    print('The number of categories has been set to ' + len(categories))
    NUM_CATEGORIES = len(categories)

# sets number of rounds for game
os.system(f"say How many rounds would you like to play?: ")
NUM_ROUNDS = input("How many rounds would you like to play?: ")

while type(NUM_CATEGORIES) != int:
    print(NUM_ROUNDS + "is not a valid number.")
    NUM_ROUNDS = input("How many rounds would you like to play?: ")

# plays game
round_counter = 0
is_game_playing = True
while True:
    os.system("say Shuffling letters")
    random.shuffle(letters)
    for letter in letters:
        # checks round count to see if game should continue
        if round_counter < NUM_ROUNDS:
            os.system(f"Round {round_counter + 1}")
            round_counter += 1
        else:
            is_game_playing = False
            break
        # say categories for round
        os.system(f"say The categories for this round are ")
        category_nums = np.random.choice(len(categories), NUM_CATEGORIES, replace=False)
        time.sleep(3)
        for i in range(NUM_CATEGORIES):
            os.system(f"say {categories[category_nums[i]]}")
            time.sleep(3)

        # say letter for round
        os.system(f"say And the letter for this round is")
        time.sleep(3)
        os.system(f"say {letter}")

        flag = False
        while not flag:
            poop = input("Press enter for next set, type 'repeat' to repeat set: ")

            if poop.lower() == "":
                flag = True
            elif poop.lower() == "repeat":
                # repeat categories for round
                os.system(f"say The categories for this round are ")
                category_nums = np.random.choice(len(categories), NUM_CATEGORIES, replace=False)
                time.sleep(3)
                for i in range(NUM_CATEGORIES):
                    os.system(f"say {categories[category_nums[i]]}")
                    time.sleep(3)

                # repeat letter for round
                os.system(f"say And the letter for this round is")
                time.sleep(3)
                os.system(f"say {letter}")
    if not is_game_playing:
        os.system(f"The game has finished!")
        break
