#!/usr/bin/env python3
import random

questions = {
   "Which country won the battle of Austerlitz?": ["France", "Russia", "England", "Germany"],
   "Who was NOT a political leader during WW2?": ["Woodrow Wilson", "Joseph Stalin", "Winston Churchill", "Benito Mussolini"]
}

def start_quiz():
    print("\nWelcome to the {} quiz show!".format(__name__))
    global score
    score = 0
      
def ask_question(key):
    print("\n{}".format(key))
    options = generate_options(questions[key])
    return options

def generate_options(option_list):
    options = {"a":"", "b":"", "c":"", "d":""}
    shuffled_options = random.sample(option_list, len(option_list))
    for key in options:
        options[key] = shuffled_options.pop(0)
    print(options)
    return (options)

def check_answer(player_answer, correct_answer, options_dict):
    return options_dict[player_answer] == correct_answer

start_quiz()
for key in questions:
    options = ask_question(key)
    correct_answer = questions[key][0]
    player_answer = input("Enter choice: ")
    result = check_answer(player_answer, correct_answer, options)
    print(result)
    print(score)

