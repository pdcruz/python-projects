#!/usr/bin/env python3
import random

### SECTION - QUESTION DATA ###
# Dictionary of all questions and answer options,
# Correct answer MUST be first item of the options list!
# Option order is randomized before presenting to the player.
questions = {
   "Which country won the battle of Austerlitz?": ["France", "Russia", "England", "Germany"],
   "Who was NOT a political leader during WW2?": ["Woodrow Wilson", "Joseph Stalin", "Winston Churchill", "Benito Mussolini"]
}

### END SECTION - QUESTION DATA ###


### SECTION - FUNCTIONS ###
def ask_question(key):
    print("\n{}".format(key))
    options = generate_options(questions[key])
    return options

def generate_options(option_list):
    options = {"a":"", "b":"", "c":"", "d":""}
    shuffled_options_list = random.sample(option_list, len(option_list))
    for key in options:
        options[key] = shuffled_options_list.pop(0)
    print(options)
    return (options)

def check_answer(player_answer, correct_answer, options_dict):
    return options_dict[player_answer] == correct_answer

### END SECTION - FUNCTIONS ###


### SECTION - MAIN ###
input("\nWelcome to the {} quiz show!\n\nPress Enter to begin ".format(__name__))
score = 0

for key in questions:
    correct_answer = questions[key][0]
    options = ask_question(key)
    player_answer = input("Enter choice: ")
    result = check_answer(player_answer, correct_answer, options)
    print(result)
    score += result

print("\nYour score: {0}/{1}".format(score, len(questions)))

### END SECTION - MAIN ###
